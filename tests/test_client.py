from pytest import raises

from ishareslib.client import Client


def generate_products_mock(requests_mock, fields: list[dict]):
    products_url = (
        "https://www.ishares.com/us/product-screener/product-screener-v3.1.jsn?dcrPath=/templatedata"
        "/config/product-screener-v3/data/en/us-ishares/ishares-product-screener-backend-config"
        "&siteEntryPassthrough=true"
    )

    fields_json: dict = {}
    for key, field in list(enumerate(fields)):
        fields_json["%d" % (23000 + key)] = field

    requests_mock.get(products_url, json=fields_json)


def test_get_product_with_different_ticker_names(requests_mock):
    generate_products_mock(requests_mock, [{"localExchangeTicker": "MCHI"}])

    client = Client()
    for ticker in ["MCHI", "mchi", "mChI"]:
        assert client.get_local_exchange_ticker(ticker) == "MCHI"


def test_get_product_with_unknown_ticker_name(requests_mock):
    generate_products_mock(requests_mock, [{"localExchangeTicker": "MCHI"}])

    client = Client()
    with raises(ValueError) as exc_info:
        client.get_local_exchange_ticker("MCH1")
    exception_raised = exc_info.value
    assert str(exception_raised) == "Ticker symbol not found! [ticker_symbol=MCH1]"


def test_get_product_with_duplicate_ticker_name(requests_mock):
    generate_products_mock(
        requests_mock,
        [{"localExchangeTicker": "MCHI"}, {"localExchangeTicker": "mChI"}],
    )

    client = Client()
    with raises(ValueError) as exc_info:
        client.get_local_exchange_ticker("mchi")
    exception_raised = exc_info.value
    assert (
        str(exception_raised)
        == "Ticker symbol needs to be unique! [ticker_symbol=mchi, result_count=2]"
    )


def test_get_product_with_str_values(requests_mock):
    generate_products_mock(
        requests_mock,
        [
            {
                "localExchangeTicker": "MCHI",
                "aladdinAssetClass": "Equity",
                "aladdinAssetClassCode": "12377",
                "aladdinCountry": "-",
                "aladdinCountryCode": "-",
                "aladdinMarketType": "-",
                "aladdinMarketTypeCode": "-",
            }
        ],
    )

    client = Client()
    assert client.get_aladdin_asset_class("MCHI") == "Equity"
    assert client.get_aladdin_asset_class_code("MCHI") == "12377"
    assert client.get_aladdin_country("MCHI") is None
    assert client.get_aladdin_country_code("MCHI") is None
    assert client.get_aladdin_esg_classification("MCHI") is None
    assert client.get_aladdin_esg_classification_code("MCHI") is None
    assert client.get_aladdin_market_type("MCHI") is None
    assert client.get_aladdin_market_type_code("MCHI") is None
    assert client.get_aladdin_region("MCHI") is None
    assert client.get_aladdin_region_code("MCHI") is None
    assert client.get_aladdin_sub_asset_class("MCHI") is None
    assert client.get_aladdin_sub_asset_class_code("MCHI") is None
    assert client.get_bid_price_formatted("MCHI") is None
    assert client.get_clean_duration_formatted("MCHI") is None
    assert client.get_cusip("MCHI") is None
    assert client.get_daily_performance_year_to_date_formatted("MCHI") is None
    assert client.get_effective_duration_formatted("MCHI") is None
    assert client.get_esg_coverage_formatted("MCHI") is None
    assert client.get_esg_msci_quality_score_as_of_date_formatted("MCHI") is None
    assert client.get_esg_msci_quality_score_formatted("MCHI") is None
    assert client.get_esg_rating("MCHI") is None
    assert client.get_esg_report_holding_as_of_date_formatted("MCHI") is None
    assert client.get_esg_suite_category("MCHI") is None
    assert client.get_esg_suite_category_code("MCHI") is None
    assert client.get_fees_formatted("MCHI") is None
    assert client.get_fund_name("MCHI") is None
    assert client.get_inception_date_formatted("MCHI") is None
    assert client.get_investment_style("MCHI") is None
    assert client.get_investment_style_code("MCHI") is None
    assert client.get_investor_class_name("MCHI") is None
    assert client.get_isin("MCHI") is None
    assert client.get_local_exchange_ticker("MCHI") == "MCHI"
    assert client.get_merged_esg_as_of_dates_formatted("MCHI") is None
    assert client.get_mgt_formatted("MCHI") is None
    assert client.get_model_oad_effective_duration_formatted("MCHI") is None
    assert client.get_model_oad_formatted("MCHI") is None
    assert client.get_nav_amount_as_of_formatted("MCHI") is None
    assert client.get_nav_amount_formatted("MCHI") is None
    assert client.get_nav_annualised_as_of_formatted("MCHI") is None
    assert client.get_nav_five_year_annualized_formatted("MCHI") is None
    assert client.get_nav_one_year_annualized_formatted("MCHI") is None
    assert client.get_nav_perf_as_of_formatted("MCHI") is None
    assert client.get_nav_since_inception_annualized_formatted("MCHI") is None
    assert client.get_nav_ten_year_annualized_formatted("MCHI") is None
    assert client.get_nav_three_year_annualized_formatted("MCHI") is None
    assert client.get_nav_year_to_date_formatted("MCHI") is None
    assert client.get_netr_formatted("MCHI") is None
    assert client.get_option_adjusted_spread_as_of_formatted("MCHI") is None
    assert client.get_option_adjusted_spread_formatted("MCHI") is None
    assert client.get_price_five_year_annualized_formatted("MCHI") is None
    assert client.get_price_one_year_annualized_formatted("MCHI") is None
    assert client.get_price_since_inception_annualized_formatted("MCHI") is None
    assert client.get_price_ten_year_annualized_formatted("MCHI") is None
    assert client.get_price_three_year_annualized_formatted("MCHI") is None
    assert client.get_price_year_as_of_formatted("MCHI") is None
    assert client.get_price_year_to_date_formatted("MCHI") is None
    assert client.get_product_page_url("MCHI") is None
    assert client.get_quarterly_nav_as_of_formatted("MCHI") is None
    assert client.get_quarterly_nav_five_year_annualized_formatted("MCHI") is None
    assert client.get_quarterly_nav_one_year_annualized_formatted("MCHI") is None
    assert client.get_quarterly_nav_since_inception_annualized_formatted("MCHI") is None
    assert client.get_quarterly_nav_ten_year_annualized_formatted("MCHI") is None
    assert client.get_quarterly_nav_three_year_annualized_formatted("MCHI") is None
    assert client.get_quarterly_nav_year_to_date_formatted("MCHI") is None
    assert client.get_quarterly_price_as_of_formatted("MCHI") is None
    assert client.get_quarterly_price_five_year_annualized_formatted("MCHI") is None
    assert client.get_quarterly_price_one_year_annualized_formatted("MCHI") is None
    assert (
        client.get_quarterly_price_since_inception_annualized_formatted("MCHI") is None
    )
    assert client.get_quarterly_price_ten_year_annualized_formatted("MCHI") is None
    assert client.get_quarterly_price_three_year_annualized_formatted("MCHI") is None
    assert client.get_quarterly_price_year_to_date_formatted("MCHI") is None
    assert client.get_sedol("MCHI") is None
    assert client.get_ter_formatted("MCHI") is None
    assert client.get_thirty_day_sec_yield_as_of_formatted("MCHI") is None
    assert client.get_thirty_day_sec_yield_formatted("MCHI") is None
    assert client.get_total_net_assets_formatted("MCHI") is None
    assert client.get_total_net_assets_fund_as_of_formatted("MCHI") is None
    assert client.get_total_net_assets_fund_formatted("MCHI") is None
    assert client.get_twelve_mon_trl_yield_as_of_formatted("MCHI") is None
    assert client.get_twelve_mon_trl_yield_formatted("MCHI") is None
    assert client.get_unsubsidized_yield_formatted("MCHI") is None
    assert client.get_wtd_avg_carbon_intensity_formatted("MCHI") is None
    assert client.get_yield_to_worst_as_of_formatted("MCHI") is None
    assert client.get_yield_to_worst_formatted("MCHI") is None


def test_get_product_with_int_values(requests_mock):
    generate_products_mock(
        requests_mock,
        [
            {
                "localExchangeTicker": "MCHI",
                "esgMsciQualityScoreAsOfDate": {"r": 12883},
                "esgReportHoldingAsOfDate": {"r": 13.4483},
                "inceptionDate": "-",
            }
        ],
    )

    client = Client()
    assert client.get_esg_msci_quality_score_as_of_date("MCHI") == 12883
    assert client.get_esg_report_holding_as_of_date("MCHI") is None
    assert client.get_inception_date("MCHI") is None
    assert client.get_merged_esg_as_of_dates("MCHI") is None
    assert client.get_nav_amount_as_of("MCHI") is None
    assert client.get_nav_annualised_as_of("MCHI") is None
    assert client.get_nav_perf_as_of("MCHI") is None
    assert client.get_option_adjusted_spread_as_of("MCHI") is None
    assert client.get_portfolio_id("MCHI") is None
    assert client.get_price_year_as_of("MCHI") is None
    assert client.get_quarterly_nav_as_of("MCHI") is None
    assert client.get_quarterly_price_as_of("MCHI") is None
    assert client.get_thirty_day_sec_yield_as_of("MCHI") is None
    assert client.get_total_net_assets_fund_as_of("MCHI") is None
    assert client.get_twelve_mon_trl_yield_as_of("MCHI") is None
    assert client.get_yield_to_worst_as_of("MCHI") is None


def test_get_product_with_float_values(requests_mock):
    generate_products_mock(
        requests_mock,
        [
            {
                "localExchangeTicker": "MCHI",
                "bidPrice": {"r": 13.4483},
                "cleanDuration": {"r": 12883},
                "dailyPerformanceYearToDate": "-",
            }
        ],
    )

    client = Client()
    assert client.get_bid_price("MCHI") == 13.4483
    assert client.get_clean_duration("MCHI") is None
    assert client.get_daily_performance_year_to_date("MCHI") is None
    assert client.get_effective_duration("MCHI") is None
    assert client.get_esg_coverage("MCHI") is None
    assert client.get_esg_msci_quality_score("MCHI") is None
    assert client.get_fees("MCHI") is None
    assert client.get_mgt("MCHI") is None
    assert client.get_model_oad("MCHI") is None
    assert client.get_model_oad_effective_duration("MCHI") is None
    assert client.get_nav_amount("MCHI") is None
    assert client.get_nav_five_year_annualized("MCHI") is None
    assert client.get_nav_one_year_annualized("MCHI") is None
    assert client.get_nav_since_inception_annualized("MCHI") is None
    assert client.get_nav_ten_year_annualized("MCHI") is None
    assert client.get_nav_three_year_annualized("MCHI") is None
    assert client.get_nav_year_to_date("MCHI") is None
    assert client.get_netr("MCHI") is None
    assert client.get_option_adjusted_spread("MCHI") is None
    assert client.get_price_five_year_annualized("MCHI") is None
    assert client.get_price_one_year_annualized("MCHI") is None
    assert client.get_price_since_inception_annualized("MCHI") is None
    assert client.get_price_ten_year_annualized("MCHI") is None
    assert client.get_price_three_year_annualized("MCHI") is None
    assert client.get_price_year_to_date("MCHI") is None
    assert client.get_quarterly_nav_five_year_annualized("MCHI") is None
    assert client.get_quarterly_nav_one_year_annualized("MCHI") is None
    assert client.get_quarterly_nav_since_inception_annualized("MCHI") is None
    assert client.get_quarterly_nav_ten_year_annualized("MCHI") is None
    assert client.get_quarterly_nav_three_year_annualized("MCHI") is None
    assert client.get_quarterly_nav_year_to_date("MCHI") is None
    assert client.get_quarterly_price_five_year_annualized("MCHI") is None
    assert client.get_quarterly_price_one_year_annualized("MCHI") is None
    assert client.get_quarterly_price_since_inception_annualized("MCHI") is None
    assert client.get_quarterly_price_ten_year_annualized("MCHI") is None
    assert client.get_quarterly_price_three_year_annualized("MCHI") is None
    assert client.get_quarterly_price_year_to_date("MCHI") is None
    assert client.get_ter("MCHI") is None
    assert client.get_thirty_day_sec_yield("MCHI") is None
    assert client.get_total_net_assets("MCHI") is None
    assert client.get_total_net_assets_fund("MCHI") is None
    assert client.get_twelve_mon_trl_yield("MCHI") is None
    assert client.get_unsubsidized_yield("MCHI") is None
    assert client.get_wtd_avg_carbon_intensity("MCHI") is None
    assert client.get_yield_to_worst("MCHI") is None


def test_get_product_with_list_values(requests_mock):
    generate_products_mock(
        requests_mock,
        [
            {
                "localExchangeTicker": "MCHI",
                "esg.alternatives": [25663, 2344],
                "productRange": [["etf", "extra"]],
                "dailyPerformanceYearToDate": "-",
            }
        ],
    )

    client = Client()
    assert client.get_esg_alternatives("MCHI") == [25663, 2344]
    assert client.get_product_range("MCHI") == [["etf", "extra"]]
    assert client.get_product_range_code("MCHI") is None
    assert client.get_product_view("MCHI") is None


def test_clear():
    client = Client()
    assert client._cached_products_df is None
    client.get_products()
    assert client._cached_products_df is not None
    client.clear()
    assert client._cached_products_df is None
