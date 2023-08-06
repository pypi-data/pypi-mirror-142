import asyncio
import json
import aio_pika
import typing
import os
import logging

from hw_event_ingress.registry import EventRoute

logger = logging.getLogger(__name__)
RABBIT_EXCHANGE = os.getenv("RABBIT_EXCHANGE", "events_hep18")
RABBIT_HEADER_EXCHANGE = os.getenv("RABBIT_HEADER_EXCHANGE", "events_hep18_hx")
RABBIT_DL_EXCHANGE = os.getenv("RABBIT_DEAD_LETTER_EXCHANGE", "worker_dl_exchange")
RABBIT_DL_QUEUE = os.getenv("RABBIT_DEAD_LETTER_QUEUE", "worker_dl_queue")
RABBIT_USER = os.getenv("RABBIT_USER", "guest")
RABBIT_PASS = os.getenv("RABBIT_PASS", "guest")
RABBIT_URL = os.getenv("RABBIT_URL", os.getenv("RABBIT_HOST", "localhost"))
RABBIT_PORT = int(os.getenv("RABBIT_PORT", 5672))
RABBIT_PREFETCH = int(os.getenv("RABBIT_PREFETCH", 10))


class RabbitCredentials:
    def __init__(
        self,
        host: str = RABBIT_URL,
        exchange: str = RABBIT_EXCHANGE,
        header_exchange: str = RABBIT_HEADER_EXCHANGE,
        dead_letter_exchange: str = RABBIT_DL_EXCHANGE,
        dead_letter_queue: str = RABBIT_DL_QUEUE,
        username: str = RABBIT_USER,
        password: str = RABBIT_PASS,
        port: int = RABBIT_PORT,
        prefetch_count: int = RABBIT_PREFETCH,
    ) -> None:
        self.url = host
        self.exchange = exchange
        self.header_exchange = header_exchange
        self.dead_letter_exchange = dead_letter_exchange
        self.dead_letter_queue = dead_letter_queue
        self.username = username
        self.password = password
        self.port = port
        self.prefetch_count = prefetch_count


class Rabbit:
    def __init__(
        self,
        hrn: bool = False,
        credentials: typing.Union[None, RabbitCredentials] = None,
    ):
        self.bootstrapped = False
        self.creds: RabbitCredentials = (
            credentials if credentials else RabbitCredentials()
        )
        self.hrn: bool = hrn
        self.callbacks: typing.Dict[
            str, typing.List[typing.Callable[..., typing.Any]]
        ] = {}
        self.connection: typing.Union[
            aio_pika.RobustConnection, aio_pika.Connection, None
        ] = None
        self.channel: typing.Union[aio_pika.RobustChannel, None] = None
        self.exchange: typing.Union[
            aio_pika.RobustExchange, aio_pika.Exchange, None
        ] = None
        self.exchange_hx: typing.Union[
            aio_pika.RobustExchange, aio_pika.Exchange, None
        ] = None
        self.dl_exchange: typing.Union[
            aio_pika.RobustExchange, aio_pika.Exchange, None
        ] = None
        self.queue: typing.Union[aio_pika.RobustQueue, aio_pika.Queue, None] = None
        self.queues: typing.List[typing.Union[aio_pika.RobustQueue]] = []
        self.dl_queue: typing.Union[aio_pika.RobustQueue, aio_pika.Queue, None] = None

    async def setup(self) -> None:
        exchange = self.creds.exchange
        exchange_type = aio_pika.ExchangeType.TOPIC
        if self.hrn:
            exchange = self.creds.header_exchange
            exchange_type = aio_pika.ExchangeType.HEADERS

        # ensure exchanges exists
        if not self.channel:
            raise Exception("channel not found")
        self.exchange = await self.channel.declare_exchange(
            exchange, exchange_type, durable=True, robust=True
        )
        self.dl_exchange = await self.channel.declare_exchange(
            self.creds.dead_letter_exchange,
            aio_pika.ExchangeType.TOPIC,
            durable=True,
            robust=True,
        )

        # default queue arguments
        dlq_args = {"x-queue-type": "quorum"}

        # create our dead letter queue and bind it to our dead letter exchange
        self.dl_queue = await self.channel.declare_queue(
            self.creds.dead_letter_exchange,
            arguments=dlq_args,
            durable=True,
            robust=True,
        )
        await self.dl_queue.bind(self.creds.dead_letter_exchange, routing_key="#")

    async def consume(
        self,
        callback_wrapper: typing.Union[typing.Callable[..., typing.Any], None] = None,
    ) -> None:
        async def cb(
            queue: aio_pika.RobustQueue,
            handler: typing.Callable[
                [str, aio_pika.IncomingMessage], typing.Awaitable[typing.Any]
            ],
        ) -> None:
            async with queue.iterator() as _q:
                async for message in _q:
                    if callback_wrapper:
                        await callback_wrapper(handler(queue.name, message))
                        continue
                    await handler(queue.name, message)

        jobs = []
        for q in self.queues:
            jobs.append(asyncio.create_task(cb(q, self.rabbithandler)))

        await asyncio.wait(jobs)

    async def connect(self, service_name: str = "rabbitworker") -> None:
        logger.info("Obtaining new rabbitmq connection")
        for _ in range(10):
            # try to connect 10 times
            try:
                connection: aio_pika.RobustConnection = await aio_pika.connect_robust(
                    f"amqp://{self.creds.username}:{self.creds.password}@{self.creds.url}:{self.creds.port}/",
                    client_properties={"client_properties": {"service": service_name}},
                )
                break
            except ConnectionError:
                # try again
                await asyncio.sleep(3)
        else:
            raise ConnectionError(
                f"Could not connect to rabbit at {self.creds.url} "
                f"with username {self.creds.username}"
            )

        channel: aio_pika.RobustChannel = await connection.channel(
            on_return_raises=True
        )
        await channel.set_qos(prefetch_count=int(self.creds.prefetch_count))
        self.connection = connection
        self.channel = channel
        logger.info("Connected to rabbitmq...")

    async def register_queues(self, queue_name: str) -> typing.Any:
        q_args = {
            "x-queue-type": "quorum",
            "x-dead-letter-exchange": self.creds.dead_letter_exchange,
        }
        if not self.channel:
            raise Exception("channel not found")
        return await self.channel.declare_queue(
            queue_name, arguments=q_args, durable=True, robust=True
        )

    async def bind_events(self, route_map: typing.List[EventRoute]) -> None:
        if not self.bootstrapped:
            await self.connect()  # connect to rabbitmq
            await self.setup()  # bootstrap rmq
            self.bootstrapped = True
        exchange = self.creds.header_exchange
        if self.hrn:
            exchange = self.creds.exchange
        for route in route_map:
            for r in route.handlers.keys():
                # route_map.queue
                q = await self.register_queues(route.queue)
                if route.queue not in [_q.name for _q in self.queues]:
                    self.queues.append(q)
                topic = route.prefix + "." + r
                q_args = {"x-match": "all", "hw-action": topic}
                await q.bind(exchange, arguments=q_args)
                for func in route.handlers[r]:
                    self.bind_event(q, topic, func)

    def bind_event(self, queue_name: str, topic: str, callback: typing.Any) -> None:
        topic = f"{queue_name}-{topic}"
        if not self.callbacks.get(topic):
            self.callbacks.update({topic: []})
        self.callbacks[topic].append(callback)

    async def rabbithandler(
        self, queue_name: str, message: aio_pika.IncomingMessage
    ) -> None:
        retry_delay = 1
        number_of_tries = 0
        try:
            # This means we have tried it once, and will delay a retry retry_delay seconds
            if message.headers.get("x-delivery-count", False):
                await asyncio.sleep(retry_delay)
            msg_meta: typing.Dict[
                str, typing.Union[typing.Any, typing.Dict[str, typing.Any]]
            ] = {
                "consumer_tag": message.consumer_tag,
                "correlation_id": message.correlation_id,
                "headers": dict(message.headers),
                "message_id": message.message_id,
                "routing_key": message.routing_key,
                "redelivered": message.redelivered,
            }
            topic = msg_meta["headers"]["hw-action"]
            if not topic:
                topic = message.routing_key
            await self.handle_rmq_message(
                queue_name, topic, str(message.body.decode()), msg_meta
            )
            await message.ack()

        except Exception as e:
            logger.error(f"Something bad has happened {e}")
            # This requeue logic will allow you to try 3 times, otherwise send to DL exchange
            requeue = (
                number_of_tries != 0
                and message.headers.get("x-delivery-count", 0) < number_of_tries - 1
            )
            await message.reject(requeue=requeue)
            raise e

    async def handle_rmq_message(
        self, queue_name: str, topic: str, payload: str, msg_meta: typing.Any
    ) -> None:
        topic = f"{queue_name}-{topic}"
        if topic in self.callbacks.keys():
            for callback in self.callbacks[topic]:
                payload = json.loads(payload)
                await asyncio.ensure_future(callback(payload, msg_meta))
