from typing import Union

from pytest import raises

from ishareslib.core.proxy_adapter import Proxy, ProxyAdapter


class DummyProxyAdapter(ProxyAdapter):
    first = Proxy("my-dummy-proxy.local", 1000)
    second = Proxy("my-dummy-proxy.local", 1001)
    third = Proxy("my-dummy-proxy.local", 1002)
    fourth = Proxy("my-dummy-proxy.local", 1003)

    def __init__(self, proxies: list[Proxy], regeneration_limit: int = 3):
        super().__init__(regeneration_limit=regeneration_limit)
        self._proxies = proxies
        self._call_counter = 0

    def _gen_proxy(self) -> Union[Proxy, None]:
        if len(self._proxies) <= self._call_counter:
            return None
        proxy = self._proxies[self._call_counter]
        self._call_counter += 1
        return proxy


def test_get_proxy():
    adapter = DummyProxyAdapter([DummyProxyAdapter.first, DummyProxyAdapter.second])
    first_proxy = adapter.get_proxy()
    second_proxy = adapter.get_proxy()
    assert first_proxy == second_proxy


def test_get_proxy_with_no_data():
    adapter = DummyProxyAdapter([])
    with raises(ValueError) as exc_info:
        adapter.get_proxy()
    exception_raised = exc_info.value
    assert str(exception_raised) == "Could not choose a new proxy"


def test_new_proxy():
    adapter = DummyProxyAdapter([DummyProxyAdapter.first, DummyProxyAdapter.second])
    first_proxy = adapter.get_proxy()
    second_proxy = adapter.new_proxy()
    assert DummyProxyAdapter.first == first_proxy
    assert DummyProxyAdapter.second == second_proxy


def test_new_with_get_proxy():
    adapter = DummyProxyAdapter([DummyProxyAdapter.first, DummyProxyAdapter.second])
    first_proxy = adapter.new_proxy()
    second_proxy = adapter.get_proxy()
    third_proxy = adapter.new_proxy()
    fourth_proxy = adapter.get_proxy()
    assert DummyProxyAdapter.first == first_proxy
    assert first_proxy == second_proxy
    assert DummyProxyAdapter.second == third_proxy
    assert third_proxy == fourth_proxy


def test_new_proxy_with_same_entities():
    adapter = DummyProxyAdapter(
        [
            DummyProxyAdapter.first,
            DummyProxyAdapter.second,
            DummyProxyAdapter.second,
            DummyProxyAdapter.third,
        ]
    )
    first_proxy = adapter.new_proxy()
    second_proxy = adapter.new_proxy()
    third_proxy = adapter.new_proxy()
    assert DummyProxyAdapter.first == first_proxy
    assert DummyProxyAdapter.second == second_proxy
    assert DummyProxyAdapter.third == third_proxy


def test_new_proxy_with_regeneration_level_exceeded():
    adapter = DummyProxyAdapter(
        [
            DummyProxyAdapter.first,
            DummyProxyAdapter.second,
            DummyProxyAdapter.second,
            DummyProxyAdapter.second,
            DummyProxyAdapter.third,
        ],
        regeneration_limit=2,
    )
    adapter.new_proxy()
    adapter.new_proxy()
    with raises(ValueError) as exc_info:
        adapter.new_proxy()
    exception_raised = exc_info.value
    assert str(exception_raised) == "Proxy regeneration limit exceeded"
