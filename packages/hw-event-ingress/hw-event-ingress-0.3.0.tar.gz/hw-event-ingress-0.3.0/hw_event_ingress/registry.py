import typing


class EventRoute:
    def __init__(self, prefix: str = "", queue: str = "generic_worker") -> None:
        self.prefix = prefix
        self.handlers: typing.Dict[str, typing.List[typing.Callable[..., None]]] = {}
        self.queue = queue

    def handle_event(
        self, route_keys: typing.List[str]
    ) -> typing.Callable[..., typing.Callable[..., None]]:
        def wrapper(func: typing.Callable[..., None]) -> typing.Callable[..., None]:
            # TODO: handle prefix eg records.*
            for route_key in route_keys:
                if route_key not in self.handlers.keys():
                    self.handlers[route_key] = []
                self.handlers[route_key].append(func)
            return func

        return wrapper


class EventRoutes:
    def __init__(self, routes: typing.List[EventRoute]) -> None:
        self.routes = routes
