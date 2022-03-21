from random import choice
from typing import Union

from requests import get

from ishareslib.core.proxy_adapter import Proxy, ProxyAdapter


class WebShareProxyAdapter(ProxyAdapter):
    def __init__(self, key: str, page: Union[int, None] = None):
        super().__init__()
        self._key: str = key
        self._page: Union[int, None] = page
        self._host: str = "https://proxy.webshare.io/api"
        self._proxies: list[Proxy] = []

    def new_proxy(self) -> Proxy:
        self._before_new_proxy()
        return super().new_proxy()

    def _before_new_proxy(self) -> None:
        if len(self._proxies) == 0:
            self._get_proxy_list(
                "%s/proxy/list/?page=%d" % (self._host, self._page or 1)
            )

    def _gen_proxy(self) -> Union[Proxy, None]:
        return choice(self._proxies)

    def _get_proxy_list(self, url: str):
        response = get(url, headers={"Authorization": "Token %s" % self._key}).json()
        for result in response["results"]:
            if result["valid"]:
                self._proxies.append(
                    Proxy(
                        address=result["proxy_address"],
                        port=result["ports"]["http"],
                        username=result["username"],
                        password=result["password"],
                    )
                )

        if self._page is None and response["next"] is not None:
            self._get_proxy_list(response["next"])
