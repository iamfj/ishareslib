from abc import ABC, abstractmethod

from ishareslib.core.proxy import Proxy


class ProxyFactory(ABC):
    def __init__(self):
        self._proxy = None

    def get_proxy(self) -> Proxy:
        if self._proxy is None:
            return self.new_proxy()
        return self._proxy

    @abstractmethod
    def new_proxy(self) -> Proxy:
        pass
