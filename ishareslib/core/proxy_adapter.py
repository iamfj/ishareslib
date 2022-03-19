from abc import ABC, abstractmethod


class Proxy:
    def __init__(
        self,
        address: str,
        port: int,
        protocol: str = "http",
        username: str = None,
        password: str = None,
    ):
        self.address = address
        self.port = port
        self.protocol = protocol
        self.username = username
        self.password = password


class ProxyAdapter(ABC):
    def __init__(self):
        self._proxy = None

    def get_proxy(self) -> Proxy:
        if self._proxy is None:
            self._proxy = self.new_proxy()
        return self._proxy

    @abstractmethod
    def new_proxy(self) -> Proxy:
        pass
