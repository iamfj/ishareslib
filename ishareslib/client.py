from typing import Union

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

    def get_holdings(self, ticker_symbol: str) -> DataFrame:
        product = self.get_product(ticker_symbol)
        return read_csv(
            "%s%s/1467271812596.ajax?fileType=csv"
            % (self._host, product["productPageUrl"]),
            skiprows=9,
        )

    @staticmethod
    def _get_or_none(value, none_value: str = "-") -> Union[str, None]:
        if not isinstance(value, str) or value == none_value:
            return None
        return value

    def get_aladdin_asset_class(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["aladdinAssetClass"])

    def get_aladdin_asset_class_code(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["aladdinAssetClassCode"]
        )

    def get_aladdin_country(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["aladdinCountry"])

    def get_aladdin_country_code(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["aladdinCountryCode"]
        )

    def get_aladdin_esg_classification(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["aladdinEsgClassification"]
        )

    def get_aladdin_esg_classification_code(
        self, ticker_symbol: str
    ) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["aladdinEsgClassificationCode"]
        )

    def get_aladdin_market_type(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["aladdinMarketType"])

    def get_aladdin_market_type_code(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["aladdinMarketTypeCode"]
        )

    def get_aladdin_region(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["aladdinRegion"])

    def get_aladdin_region_code(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["aladdinRegionCode"])

    def get_aladdin_sub_asset_class(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["aladdinSubAssetClass"]
        )

    def get_aladdin_sub_asset_class_code(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["aladdinSubAssetClassCode"]
        )

    def get_clean_duration(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["cleanDuration"]["r"]

    def get_clean_duration_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["cleanDuration"]["d"]

    def get_cusip(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["cusip"])

    def get_daily_performance_year_to_date(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["dailyPerformanceYearToDate"]["r"]

    def get_daily_performance_year_to_date_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["dailyPerformanceYearToDate"]["d"]

    def get_effective_duration(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["effectiveDuration"])

    def get_esg_coverage(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["esgCoverage"]["r"]

    def get_esg_coverage_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["esgCoverage"]["d"]

    def get_msci_quality_score(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["esgMsciQualityScore"]["r"]

    def get_msci_quality_score_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["esgMsciQualityScore"]["d"]

    def get_msci_quality_score_as_of_date(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["esgMsciQualityScoreAsOfDate"]["r"]

    def get_msci_quality_score_as_of_dat_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["esgMsciQualityScoreAsOfDate"]["d"]

    def get_esg_rating(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["esgRating"])

    def get_esg_report_holding_as_of_date(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["esgReportHoldingAsOfDate"]["r"]

    def get_esg_report_holding_as_of_date_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["esgReportHoldingAsOfDate"]["d"]

    def get_fees(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["fees"]["r"]

    def get_fees_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["fees"]["d"]

    def get_fund_name(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["fundName"])

    def get_gls_doc(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["glsDoc"])

    def get_inception_date(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["inceptionDate"]["r"]

    def get_inception_date_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["inceptionDate"]["d"]

    def get_investment_style(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["investmentStyle"])

    def get_investment_style_code(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["investmentStyleCode"]
        )

    def get_investor_class_name(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["investorClassName"])

    def get_isin(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["isin"])

    def get_local_exchange_ticker(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["localExchangeTicker"]
        )

    def get_mgt(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["mgt"]["r"]

    def get_mgt_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["mgt"]["d"]

    def get_model_oad(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["modelOad"])

    def get_nav_amount(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["navAmount"]["r"]

    def get_nav_amount_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["navAmount"]["d"]

    def get_nav_amount_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["navAmountAsOf"]["r"]

    def get_nav_amount_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["navAmountAsOf"]["d"]

    def get_nav_annualised_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["navAnnualisedAsOf"]["r"]

    def get_nav_annualised_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["navAnnualisedAsOf"]["d"]

    def get_nav_five_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["navFiveYearAnnualized"]["r"]

    def get_nav_five_year_annualized_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["navFiveYearAnnualized"]["d"]

    def get_nav_one_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["navOneYearAnnualized"]["r"]

    def get_nav_one_year_annualized_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["navOneYearAnnualized"]["d"]

    def get_nav_perf_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["navPerfAsOf"]["r"]

    def get_nav_perf_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["navPerfAsOf"]["d"]

    def get_nav_since_inception_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["navSinceInceptionAnnualized"]["r"]

    def get_nav_since_inception_annualized_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["navSinceInceptionAnnualized"]["d"]

    def get_nav_ten_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["navTenYearAnnualized"]["r"]

    def get_nav_ten_year_annualized_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["navTenYearAnnualized"]["d"]

    def get_nav_three_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["navThreeYearAnnualized"]["r"]

    def get_nav_three_year_annualized_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["navThreeYearAnnualized"]["d"]

    def get_nav_year_to_date(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["navYearToDate"]["r"]

    def get_nav_year_to_date_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["navYearToDate"]["d"]

    def get_netr(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["netr"]["r"]

    def get_netr_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["netr"]["d"]

    def get_option_adjusted_spread(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["optionAdjustedSpread"]["r"]

    def get_option_adjusted_spread_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["optionAdjustedSpread"]["d"]

    def get_option_adjusted_spread_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["optionAdjustedSpreadAsOf"]["r"]

    def get_option_adjusted_spread_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["optionAdjustedSpreadAsOf"]["d"]

    def get_portfolio_id(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["portfolioId"]

    def get_price_five_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["priceFiveYearAnnualized"]["r"]

    def get_price_five_year_annualized_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["priceFiveYearAnnualized"]["d"]

    def get_price_one_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["priceOneYearAnnualized"]["r"]

    def get_price_one_year_annualized_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["priceOneYearAnnualized"]["d"]

    def get_price_since_inception_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["priceSinceInceptionAnnualized"]["r"]

    def get_price_since_inception_annualized_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["priceSinceInceptionAnnualized"]["d"]

    def get_price_ten_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["priceTenYearAnnualized"]["r"]

    def get_price_ten_year_annualized_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["priceTenYearAnnualized"]["d"]

    def get_price_three_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["priceThreeYearAnnualized"]["r"]

    def get_price_three_year_annualized_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["priceThreeYearAnnualized"]["d"]

    def get_price_year_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["priceYearAsOf"]["r"]

    def get_price_year_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["priceYearAsOf"]["d"]

    def get_price_year_to_date(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["priceYearToDate"]["r"]

    def get_price_year_to_date_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["priceYearToDate"]["d"]

    def get_product_page_url(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["productPageUrl"]

    def get_product_view(self, ticker_symbol: str) -> list[str]:
        return self.get_product(ticker_symbol)["productView"]

    def get_quarterly_nav_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["quarterlyNavAsOf"]["r"]

    def get_quarterly_nav_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["quarterlyNavAsOf"]["d"]

    def get_quarterly_nav_five_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyNavFiveYearAnnualized"]["r"]

    def get_quarterly_nav_five_year_annualized_formatted(
        self, ticker_symbol: str
    ) -> str:
        return self.get_product(ticker_symbol)["quarterlyNavFiveYearAnnualized"]["d"]

    def get_quarterly_nav_one_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyNavOneYearAnnualized"]["r"]

    def get_quarterly_nav_one_year_annualized_formatted(
        self, ticker_symbol: str
    ) -> str:
        return self.get_product(ticker_symbol)["quarterlyNavOneYearAnnualized"]["d"]

    def get_quarterly_nav_since_inception_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyNavSinceInceptionAnnualized"][
            "r"
        ]

    def get_quarterly_nav_since_inception_annualized_formatted(
        self, ticker_symbol: str
    ) -> str:
        return self.get_product(ticker_symbol)["quarterlyNavSinceInceptionAnnualized"][
            "d"
        ]

    def get_quarterly_nav_ten_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyNavTenYearAnnualized"]["r"]

    def get_quarterly_nav_ten_year_annualized_formatted(
        self, ticker_symbol: str
    ) -> str:
        return self.get_product(ticker_symbol)["quarterlyNavTenYearAnnualized"]["d"]

    def get_quarterly_nav_three_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyNavThreeYearAnnualized"]["r"]

    def get_quarterly_nav_three_year_annualized_formatted(
        self, ticker_symbol: str
    ) -> str:
        return self.get_product(ticker_symbol)["quarterlyNavThreeYearAnnualized"]["d"]

    def get_quarterly_nav_year_to_date(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyNavYearToDate"]["r"]

    def get_quarterly_nav_year_to_date_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["quarterlyNavYearToDate"]["d"]

    def get_quarterly_price_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["quarterlyPriceAsOf"]["r"]

    def get_quarterly_price_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["quarterlyPriceAsOf"]["d"]

    def get_quarterly_price_five_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyPriceFiveYearAnnualized"]["r"]

    def get_quarterly_price_five_year_annualized_formatted(
        self, ticker_symbol: str
    ) -> str:
        return self.get_product(ticker_symbol)["quarterlyPriceFiveYearAnnualized"]["d"]

    def get_quarterly_price_one_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyPriceOneYearAnnualized"]["r"]

    def get_quarterly_price_one_year_annualized_formatted(
        self, ticker_symbol: str
    ) -> str:
        return self.get_product(ticker_symbol)["quarterlyPriceOneYearAnnualized"]["d"]

    def get_quarterly_price_since_inception_annualized(
        self, ticker_symbol: str
    ) -> float:
        return self.get_product(ticker_symbol)[
            "quarterlyPriceSinceInceptionAnnualized"
        ]["r"]

    def get_quarterly_price_since_inception_annualized_formatted(
        self, ticker_symbol: str
    ) -> str:
        return self.get_product(ticker_symbol)[
            "quarterlyPriceSinceInceptionAnnualized"
        ]["d"]

    def get_quarterly_price_ten_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyPriceTenYearAnnualized"]["r"]

    def get_quarterly_price_ten_year_annualized_formatted(
        self, ticker_symbol: str
    ) -> str:
        return self.get_product(ticker_symbol)["quarterlyPriceTenYearAnnualized"]["d"]

    def get_quarterly_price_three_year_annualized(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyPriceThreeYearAnnualized"]["r"]

    def get_quarterly_price_three_year_annualized_formatted(
        self, ticker_symbol: str
    ) -> str:
        return self.get_product(ticker_symbol)["quarterlyPriceThreeYearAnnualized"]["d"]

    def get_quarterly_price_year_to_date(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["quarterlyPriceYearToDate"]["r"]

    def get_quarterly_price_year_to_date_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["quarterlyPriceYearToDate"]["d"]

    def get_sedol(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["sedol"])

    def get_ter(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["ter"]["r"]

    def get_ter_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["ter"]["d"]

    def get_thirty_day_sec_yield(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["thirtyDaySecYield"]["r"]

    def get_thirty_day_sec_yield_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["thirtyDaySecYield"]["d"]

    def get_thirty_day_sec_yield_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["thirtyDaySecYieldAsOf"]["r"]

    def get_thirty_day_sec_yield_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["thirtyDaySecYieldAsOf"]["d"]

    def get_total_net_assets(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["totalNetAssets"]["r"]

    def get_total_net_assets_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["totalNetAssets"]["d"]

    def get_total_net_assets_fund(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["totalNetAssetsFund"]["r"]

    def get_total_net_assets_fund_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["totalNetAssetsFund"]["d"]

    def get_total_net_assets_fund_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["totalNetAssetsFundAsOf"]["r"]

    def get_total_net_assets_fund_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["totalNetAssetsFundAsOf"]["d"]

    def get_twelve_mon_trl_yield(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["twelveMonTrlYield"]["r"]

    def get_twelve_mon_trl_yield_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["twelveMonTrlYield"]["d"]

    def get_twelve_mon_trl_yield_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["twelveMonTrlYieldAsOf"]["r"]

    def get_twelve_mon_trl_yield_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["twelveMonTrlYieldAsOf"]["d"]

    def get_unsubsidized_yield(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["unsubsidizedYield"]["r"]

    def get_unsubsidized_yield_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["unsubsidizedYield"]["d"]

    def get_wtd_avg_carbon_intensity(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["wtdAvgCarbonIntensity"]["r"]

    def get_wtd_avg_carbon_intensity_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["wtdAvgCarbonIntensity"]["d"]

    def get_yield_to_worst(self, ticker_symbol: str) -> float:
        return self.get_product(ticker_symbol)["yieldToWorst"]["r"]

    def get_yield_to_worst_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["yieldToWorst"]["d"]

    def get_yield_to_worst_as_of(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["yieldToWorstAsOf"]["r"]

    def get_yield_to_worst_as_of_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["yieldToWorstAsOf"]["d"]

    def get_product_range(self, ticker_symbol: str) -> list[list[str]]:
        return self.get_product(ticker_symbol)["productRange"]

    def get_product_range_code(self, ticker_symbol: str) -> list[list[str]]:
        return self.get_product(ticker_symbol)["productRange"]

    def get_weighted_avg_yield_to_maturity(
        self, ticker_symbol: str
    ) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["weightedAvgYieldToMaturity"]
        )

    def get_merged_esg_as_of_dates(self, ticker_symbol: str) -> int:
        return self.get_product(ticker_symbol)["mergedEsgAsOfDates"]["r"]

    def get_merged_esg_as_of_dates_formatted(self, ticker_symbol: str) -> str:
        return self.get_product(ticker_symbol)["mergedEsgAsOfDates"]["d"]

    def get_esg_suite_category(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["esg.suiteCategory"])

    def get_esg_suite_category_code(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["esg.suiteCategoryCode"]
        )

    def get_ter_ofc(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["ter_ocf"])

    def get_model_oad_effective_duration(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(
            self.get_product(ticker_symbol)["modelOad_effectiveDuration"]
        )

    def get_bid_price(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["bidPrice"])

    def get_esg_alternatives(self, ticker_symbol: str) -> Union[str, None]:
        return Client._get_or_none(self.get_product(ticker_symbol)["esg.alternatives"])
