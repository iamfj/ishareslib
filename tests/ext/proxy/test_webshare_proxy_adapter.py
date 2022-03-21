from typing import Union

from faker import Faker
from faker.providers import internet

from ishareslib.ext.proxy.webshare_proxy_adapter import WebShareProxyAdapter


def generate_list_mock(requests_mock, faker: Faker, pages: int = 1):
    list_url = "proxy.webshare.io/api/proxy/list/?page=%d"

    for i in range(pages):
        previous_page: int = i
        current_page: int = i + 1
        next_page: int = i + 2

        previous_page_url: Union[str, None] = None
        current_page_url: str = "https://%s" % list_url % current_page
        next_page_url: Union[str, None] = None

        if previous_page > 0:
            previous_page_url = list_url % previous_page

        if next_page <= pages:
            next_page_url = list_url % next_page

        requests_mock.get(
            current_page_url,
            json={
                "count": pages,
                "next": next_page_url,
                "previous": previous_page_url,
                "results": [
                    {
                        "username": faker.user_name(),
                        "password": "jasdi2148",
                        "proxy_address": faker.ipv4(),
                        "ports": {
                            "http": faker.port_number(),
                            "socks5": faker.port_number(),
                        },
                        "valid": True,
                        "last_verification": "2019-06-09T23:34:00.095501-07:00",
                        "country_code": "US",
                        "country_code_confidence": 0.95,
                        "city_name": "New York",
                    },
                ],
            },
        )


def test_new_proxy_with_single_response(requests_mock):
    faker: Faker = Faker()
    faker.add_provider(internet)

    generate_list_mock(requests_mock, faker, pages=1)

    adapter = WebShareProxyAdapter("")
    proxy = adapter.get_proxy()
    assert proxy.address == "101.135.106.135"
    assert proxy.port == 8144
    assert proxy.username == "alex38"


def test_new_proxy_with_multiple_responses(requests_mock):
    faker: Faker = Faker()
    faker.add_provider(internet)

    generate_list_mock(requests_mock, faker, pages=2)

    adapter = WebShareProxyAdapter("")
    first_proxy = adapter.new_proxy()
    second_proxy = adapter.new_proxy()

    addresses = [first_proxy.address, second_proxy.address]
    assert addresses == ["38.11.179.14", "113.221.251.182"]


def test_new_proxy_with_fixed_target_page_response(requests_mock):
    faker: Faker = Faker()
    faker.add_provider(internet)

    generate_list_mock(requests_mock, faker, pages=2)

    adapter = WebShareProxyAdapter("", page=2)
    proxy = adapter.new_proxy()
    assert proxy.address == "65.198.154.34"
    assert proxy.port == 12881
    assert proxy.username == "jonathanwelch"
