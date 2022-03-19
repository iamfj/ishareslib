from random import choice

from requests import get

from ishareslib.core.proxy_adapter import Proxy, ProxyAdapter


class WebShareProxyAdapter(ProxyAdapter):
    def __init__(self, key: str, page: int = None):
        super().__init__()
        self._key = key
        self._page = page
        self._host = "https://proxy.webshare.io/api"
        self._proxies = None

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

    def new_proxy(self) -> Proxy:
        if self._proxies is None:
            self._get_proxy_list(
                "%s/proxy/list/?page=%d" % (self._host, self._page or 1)
            )

        new_proxy = choice(self._proxies)
        if new_proxy == self._proxy:
            return self.new_proxy()
        self._proxy = new_proxy
        return new_proxy
