from ishareslib.client import Client

# ToDo: Dont forget to mock all external requests


def test_get_products():
    client = Client()
    client.get_products()
    # ToDo: Add some test logic here


def test_get_product():
    client = Client()
    client.get_product("EFAV")
    # ToDo: Add some test logic here


def test_get_product_holdings():
    client = Client()
    holdings = client.get_product_holdings("EFAV")
    print(holdings["Ticker"].head(n=300))
    # ToDo: Add some test logic here
