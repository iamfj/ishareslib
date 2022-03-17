from pandas import DataFrame, read_csv, read_json

from ishareslib.config import Config


class Client:
    def __init__(self, config: Config = None):
        self._host = "https://www.ishares.com"

        if config is None:
            self._config = Config()
        else:
            self._config = config

        # ToDo: Add usage of user agent and proxy factories

    def get_products(self) -> DataFrame:
        return read_json(
            "%s/us/product-screener/product-screener-v3.1.jsn?dcrPath=/templatedata/config/product-screener-v3/data"
            "/en/us-ishares/ishares-product-screener-backend-config&siteEntryPassthrough=true "
            % self._host
        ).T

    def get_product(self, ticker_symbol: str) -> dict:
        products = self.get_products()
        matching_products = products.loc[
            products["localExchangeTicker"] == ticker_symbol
        ]
        matching_products_count = matching_products["localExchangeTicker"].count()
        if matching_products_count > 1:
            raise ValueError(
                "Ticker symbol needs to be unique! [ticker_symbol=%s, result_count=%d]"
                % (ticker_symbol, matching_products.size)
            )
        elif matching_products_count == 0:
            raise ValueError(
                "Ticker symbol not found! [ticker_symbol=%s]" % ticker_symbol
            )
        return matching_products.to_dict("records")[0]

    def get_product_holdings(self, ticker_symbol: str) -> DataFrame:
        product = self.get_product(ticker_symbol)
        return read_csv(
            "%s%s/1467271812596.ajax?fileType=csv"
            % (self._host, product["productPageUrl"]),
            skiprows=9,
        )
