from ishareslib.client import Client


def generate_products_mock(requests_mock):
    products_url = (
        "https://www.ishares.com/us/product-screener/product-screener-v3.1.jsn?dcrPath=/templatedata"
        "/config/product-screener-v3/data/en/us-ishares/ishares-product-screener-backend-config"
        "&siteEntryPassthrough=true"
    )

    requests_mock.get(
        products_url,
        json={
            "239619": {
                "aladdinAssetClass": "Equity",
                "aladdinAssetClassCode": "43511",
                "aladdinCountry": "China",
                "aladdinCountryCode": "43544",
                "aladdinEsgClassification": "-",
                "aladdinEsgClassificationCode": "-",
                "aladdinMarketType": "Emerging",
                "aladdinMarketTypeCode": "43524",
                "aladdinRegion": "Asia Pacific",
                "aladdinRegionCode": "43526",
                "aladdinSubAssetClass": "Large/Mid Cap",
                "aladdinSubAssetClassCode": "43581",
                "cleanDuration": {"d": "0.00", "r": 0.0},
                "cusip": "46429B671",
                "dailyPerformanceYearToDate": {"d": "-12.42", "r": -12.41549765526437},
                "effectiveDuration": "-",
                "esgCoverage": {"d": "99.26%", "r": 99.26},
                "esgMsciQualityScore": {"d": "5.24", "r": 5.2381},
                "esgMsciQualityScoreAsOfDate": {"d": "Feb 07, 2022", "r": 20220207},
                "esgRating": "BBB",
                "esgReportHoldingAsOfDate": {"d": "Dec 31, 2021", "r": 20211231},
                "fees": {"d": "0.57", "r": 0.57},
                "fundName": "iShares MSCI China ETF",
                "glsDoc": "-",
                "inceptionDate": {"d": "Mar 29, 2011", "r": 20110329},
                "investmentStyle": "[Index]",
                "investmentStyleCode": "[44342]",
                "investorClassName": " ",
                "isin": "US46429B6719",
                "localExchangeTicker": "MCHI",
                "mgt": {"d": "0.57", "r": 0.57},
                "modelOad": "-",
                "navAmount": {"d": "54.80", "r": 54.798781},
                "navAmountAsOf": {"d": "Mar 18, 2022", "r": 20220318},
                "navAnnualisedAsOf": {"d": "Feb 28, 2022", "r": 20220228},
                "navFiveYearAnnualized": {"d": "5.14", "r": 5.14},
                "navOneYearAnnualized": {"d": "-31.58", "r": -31.58},
                "navPerfAsOf": {"d": "Feb 28, 2022", "r": 20220228},
                "navSinceInceptionAnnualized": {"d": "3.33", "r": 3.33},
                "navTenYearAnnualized": {"d": "4.13", "r": 4.13},
                "navThreeYearAnnualized": {"d": "0.00", "r": 0.0},
                "navYearToDate": {"d": "-6.35", "r": -6.35},
                "netr": {"d": "0.57", "r": 0.57},
                "optionAdjustedSpread": {"d": "0.00", "r": 0.0},
                "optionAdjustedSpreadAsOf": {"d": "Mar 18, 2022", "r": 20220318},
                "portfolioId": 239619,
                "priceFiveYearAnnualized": {"d": "5.17", "r": 5.17},
                "priceOneYearAnnualized": {"d": "-32.07", "r": -32.07},
                "priceSinceInceptionAnnualized": {"d": "3.33", "r": 3.33},
                "priceTenYearAnnualized": {"d": "4.17", "r": 4.17},
                "priceThreeYearAnnualized": {"d": "0.05", "r": 0.05},
                "priceYearAsOf": {"d": "Feb 28, 2022", "r": 20220228},
                "priceYearToDate": {"d": "-6.63", "r": -6.63},
                "productPageUrl": "/us/products/239619/ishares-msci-china-etf",
                "productView": ["etf"],
                "quarterlyNavAsOf": {"d": "Dec 31, 2021", "r": 20211231},
                "quarterlyNavFiveYearAnnualized": {"d": "8.67", "r": 8.67},
                "quarterlyNavOneYearAnnualized": {"d": "-22.38", "r": -22.38},
                "quarterlyNavSinceInceptionAnnualized": {"d": "4.01", "r": 4.01},
                "quarterlyNavTenYearAnnualized": {"d": "6.55", "r": 6.55},
                "quarterlyNavThreeYearAnnualized": {"d": "7.01", "r": 7.01},
                "quarterlyNavYearToDate": {"d": "-22.38", "r": -22.38},
                "quarterlyPriceAsOf": {"d": "Dec 31, 2021", "r": 20211231},
                "quarterlyPriceFiveYearAnnualized": {"d": "8.96", "r": 8.96},
                "quarterlyPriceOneYearAnnualized": {"d": "-21.73", "r": -21.73},
                "quarterlyPriceSinceInceptionAnnualized": {"d": "4.04", "r": 4.04},
                "quarterlyPriceTenYearAnnualized": {"d": "6.55", "r": 6.55},
                "quarterlyPriceThreeYearAnnualized": {"d": "7.34", "r": 7.34},
                "quarterlyPriceYearToDate": {"d": "-21.73", "r": -21.73},
                "sedol": "-",
                "ter": {"d": "0.57", "r": 0.57},
                "thirtyDaySecYield": {"d": "1.15", "r": 1.1524},
                "thirtyDaySecYieldAsOf": {"d": "Feb 28, 2022", "r": 20220228},
                "totalNetAssets": {"d": "6,400,497,621", "r": 6.40049762119e9},
                "totalNetAssetsFund": {"d": "6,400,497,621", "r": 6.40049762119e9},
                "totalNetAssetsFundAsOf": {"d": "Mar 18, 2022", "r": 20220318},
                "twelveMonTrlYield": {"d": "1.12", "r": 1.1177},
                "twelveMonTrlYieldAsOf": {"d": "Feb 28, 2022", "r": 20220228},
                "unsubsidizedYield": {"d": "1.15", "r": 1.1524},
                "wtdAvgCarbonIntensity": {"d": "224.93", "r": 224.93},
                "yieldToWorst": {"d": "0.00", "r": 0.0},
                "yieldToWorstAsOf": {"d": "Mar 18, 2022", "r": 20220318},
                "productRange": [
                    ["International Equity", "Geography", "Emerging Markets"],
                    ["International Equity", "Geography", "Country Specific"],
                ],
                "productRangeCode": [["140", "141", "151"], ["140", "141", "163"]],
                "weightedAvgYieldToMaturity": "-",
                "mergedEsgAsOfDates": {
                    "d": "Feb 07, 2022 (Dec 31, 2021)",
                    "r": 20220207,
                },
                "esg.suiteCategory": "-",
                "esg.suiteCategoryCode": "-",
                "ter_ocf": "-",
                "modelOad_effectiveDuration": "-",
                "bidPrice": "-",
            },
        },
    )


def test_get_products(requests_mock):
    generate_products_mock(requests_mock)

    client = Client()
    for ticker in ["MCHI", "mchi", "mChI"]:
        assert client.get_aladdin_asset_class(ticker) == "Equity"
        assert client.get_aladdin_asset_class_code(ticker) == "43511"
        assert client.get_aladdin_country(ticker) == "China"
        assert client.get_aladdin_country_code(ticker) == "43544"
        assert client.get_aladdin_esg_classification(ticker) is None
        assert client.get_aladdin_esg_classification_code(ticker) is None
        assert client.get_aladdin_market_type(ticker) == "Emerging"
        assert client.get_aladdin_market_type_code(ticker) == "43524"
        assert client.get_aladdin_region(ticker) == "Asia Pacific"
        assert client.get_aladdin_region_code(ticker) == "43526"
        assert client.get_aladdin_sub_asset_class(ticker) == "Large/Mid Cap"
        assert client.get_aladdin_sub_asset_class_code(ticker) == "43581"
        assert client.get_clean_duration(ticker) == 0.0
        assert client.get_clean_duration_formatted(ticker) == "0.00"
        assert client.get_cusip(ticker) == "46429B671"
        assert client.get_daily_performance_year_to_date(ticker) == -12.41549765526437
        assert client.get_daily_performance_year_to_date_formatted(ticker) == "-12.42"
        assert client.get_effective_duration(ticker) is None
        assert client.get_esg_coverage(ticker) == 99.26
        assert client.get_esg_coverage_formatted(ticker) == "99.26%"
        assert client.get_esg_msci_quality_score(ticker) == 5.2381
        assert client.get_esg_msci_quality_score_formatted(ticker) == "5.24"
        assert client.get_esg_msci_quality_score_as_of_date(ticker) == 20220207
        assert (
            client.get_esg_msci_quality_score_as_of_date_formatted(ticker)
            == "Feb 07, 2022"
        )
        assert client.get_esg_rating(ticker) == "BBB"
        assert client.get_esg_report_holding_as_of_date(ticker) == 20211231
        assert (
            client.get_esg_report_holding_as_of_date_formatted(ticker) == "Dec 31, 2021"
        )
        assert client.get_fees(ticker) == 0.57
        assert client.get_fees_formatted(ticker) == "0.57"
        assert client.get_fund_name(ticker) == "iShares MSCI China ETF"
        assert client.get_gls_doc(ticker) is None
        assert client.get_inception_date(ticker) == 20110329
        assert client.get_inception_date_formatted(ticker) == "Mar 29, 2011"
        assert client.get_investment_style(ticker) == "[Index]"
        assert client.get_investment_style_code(ticker) == "[44342]"
        assert client.get_investor_class_name(ticker) == " "
        assert client.get_isin(ticker) == "US46429B6719"
        assert client.get_local_exchange_ticker(ticker) == "MCHI"
        assert client.get_mgt(ticker) == 0.57
        assert client.get_mgt_formatted(ticker) == "0.57"
        assert client.get_model_oad(ticker) is None
        assert client.get_nav_amount(ticker) == 54.798781
        assert client.get_nav_amount_formatted(ticker) == "54.80"
        assert client.get_nav_amount_as_of(ticker) == 20220318
        assert client.get_nav_amount_as_of_formatted(ticker) == "Mar 18, 2022"
        assert client.get_nav_annualised_as_of(ticker) == 20220228
        assert client.get_nav_annualised_as_of_formatted(ticker) == "Feb 28, 2022"
        assert client.get_nav_five_year_annualized(ticker) == 5.14
        assert client.get_nav_five_year_annualized_formatted(ticker) == "5.14"
        assert client.get_nav_one_year_annualized(ticker) == -31.58
        assert client.get_nav_one_year_annualized_formatted(ticker) == "-31.58"
        assert client.get_nav_perf_as_of(ticker) == 20220228
        assert client.get_nav_perf_as_of_formatted(ticker) == "Feb 28, 2022"
        assert client.get_nav_since_inception_annualized(ticker) == 3.33
        assert client.get_nav_since_inception_annualized_formatted(ticker) == "3.33"
        assert client.get_nav_ten_year_annualized(ticker) == 4.13
        assert client.get_nav_ten_year_annualized_formatted(ticker) == "4.13"
        assert client.get_nav_three_year_annualized(ticker) == 0.0
        assert client.get_nav_three_year_annualized_formatted(ticker) == "0.00"
        assert client.get_nav_year_to_date(ticker) == -6.35
        assert client.get_nav_year_to_date_formatted(ticker) == "-6.35"
        assert client.get_netr(ticker) == 0.57
        assert client.get_netr_formatted(ticker) == "0.57"
        assert client.get_option_adjusted_spread(ticker) == 0.0
        assert client.get_option_adjusted_spread_formatted(ticker) == "0.00"
        assert client.get_option_adjusted_spread_as_of(ticker) == 20220318
        assert (
            client.get_option_adjusted_spread_as_of_formatted(ticker) == "Mar 18, 2022"
        )
        assert client.get_portfolio_id(ticker) == 239619
        assert client.get_price_five_year_annualized(ticker) == 5.17
        assert client.get_price_five_year_annualized_formatted(ticker) == "5.17"
        assert client.get_price_one_year_annualized(ticker) == -32.07
        assert client.get_price_one_year_annualized_formatted(ticker) == "-32.07"
        assert client.get_price_since_inception_annualized(ticker) == 3.33
        assert client.get_price_since_inception_annualized_formatted(ticker) == "3.33"
        assert client.get_price_ten_year_annualized(ticker) == 4.17
        assert client.get_price_ten_year_annualized_formatted(ticker) == "4.17"
        assert client.get_price_three_year_annualized(ticker) == 0.05
        assert client.get_price_three_year_annualized_formatted(ticker) == "0.05"
        assert client.get_price_year_as_of(ticker) == 20220228
        assert client.get_price_year_as_of_formatted(ticker) == "Feb 28, 2022"
        assert client.get_price_year_to_date(ticker) == -6.63
        assert client.get_price_year_to_date_formatted(ticker) == "-6.63"
        assert (
            client.get_product_page_url(ticker)
            == "/us/products/239619/ishares-msci-china-etf"
        )
        assert client.get_product_view(ticker).sort() == ["etf"].sort()
        assert client.get_quarterly_nav_as_of(ticker) == 20211231
        assert client.get_quarterly_nav_as_of_formatted(ticker) == "Dec 31, 2021"
        assert client.get_quarterly_nav_five_year_annualized(ticker) == 8.67
        assert client.get_quarterly_nav_five_year_annualized_formatted(ticker) == "8.67"
        assert client.get_quarterly_nav_one_year_annualized(ticker) == -22.38
        assert (
            client.get_quarterly_nav_one_year_annualized_formatted(ticker) == "-22.38"
        )
        assert client.get_quarterly_nav_since_inception_annualized(ticker) == 4.01
        assert (
            client.get_quarterly_nav_since_inception_annualized_formatted(ticker)
            == "4.01"
        )
        assert client.get_quarterly_nav_ten_year_annualized(ticker) == 6.55
        assert client.get_quarterly_nav_ten_year_annualized_formatted(ticker) == "6.55"
        assert client.get_quarterly_nav_three_year_annualized(ticker) == 7.01
        assert (
            client.get_quarterly_nav_three_year_annualized_formatted(ticker) == "7.01"
        )
        assert client.get_quarterly_nav_year_to_date(ticker) == -22.38
        assert client.get_quarterly_nav_year_to_date_formatted(ticker) == "-22.38"
        assert client.get_quarterly_price_as_of(ticker) == 20211231
        assert client.get_quarterly_price_as_of_formatted(ticker) == "Dec 31, 2021"
        assert client.get_quarterly_price_five_year_annualized(ticker) == 8.96
        assert (
            client.get_quarterly_price_five_year_annualized_formatted(ticker) == "8.96"
        )
        assert client.get_quarterly_price_one_year_annualized(ticker) == -21.73
        assert (
            client.get_quarterly_price_one_year_annualized_formatted(ticker) == "-21.73"
        )
        assert client.get_quarterly_price_since_inception_annualized(ticker) == 4.04
        assert (
            client.get_quarterly_price_since_inception_annualized_formatted(ticker)
            == "4.04"
        )
        assert client.get_quarterly_price_ten_year_annualized(ticker) == 6.55
        assert (
            client.get_quarterly_price_ten_year_annualized_formatted(ticker) == "6.55"
        )
        assert client.get_quarterly_price_three_year_annualized(ticker) == 7.34
        assert (
            client.get_quarterly_price_three_year_annualized_formatted(ticker) == "7.34"
        )
        assert client.get_quarterly_price_year_to_date(ticker) == -21.73
        assert client.get_quarterly_price_year_to_date_formatted(ticker) == "-21.73"
        assert client.get_sedol(ticker) is None
        assert client.get_ter(ticker) == 0.57
        assert client.get_ter_formatted(ticker) == "0.57"
        assert client.get_thirty_day_sec_yield(ticker) == 1.1524
        assert client.get_thirty_day_sec_yield_formatted(ticker) == "1.15"
        assert client.get_thirty_day_sec_yield_as_of(ticker) == 20220228
        assert client.get_thirty_day_sec_yield_as_of_formatted(ticker) == "Feb 28, 2022"
        assert client.get_total_net_assets(ticker) == 6.40049762119e9
        assert client.get_total_net_assets_formatted(ticker) == "6,400,497,621"
        assert client.get_total_net_assets_fund(ticker) == 6.40049762119e9
        assert client.get_total_net_assets_fund_formatted(ticker) == "6,400,497,621"
        assert client.get_total_net_assets_fund_as_of(ticker) == 20220318
        assert (
            client.get_total_net_assets_fund_as_of_formatted(ticker) == "Mar 18, 2022"
        )
        assert client.get_twelve_mon_trl_yield(ticker) == 1.1177
        assert client.get_twelve_mon_trl_yield_formatted(ticker) == "1.12"
        assert client.get_twelve_mon_trl_yield_as_of(ticker) == 20220228
        assert client.get_twelve_mon_trl_yield_as_of_formatted(ticker) == "Feb 28, 2022"
        assert client.get_unsubsidized_yield(ticker) == 1.1524
        assert client.get_unsubsidized_yield_formatted(ticker) == "1.15"
        assert client.get_wtd_avg_carbon_intensity(ticker) == 224.93
        assert client.get_wtd_avg_carbon_intensity_formatted(ticker) == "224.93"
        assert client.get_yield_to_worst(ticker) == 0.0
        assert client.get_yield_to_worst_formatted(ticker) == "0.00"
        assert client.get_yield_to_worst_as_of(ticker) == 20220318
        assert client.get_yield_to_worst_as_of_formatted(ticker) == "Mar 18, 2022"
        assert (
            client.get_product_range(ticker).sort()
            == [
                ["International Equity", "Geography", "Emerging Markets"],
                ["International Equity", "Geography", "Country Specific"],
            ].sort()
        )
        assert (
            client.get_product_range_code(ticker).sort()
            == [["140", "141", "151"], ["140", "141", "163"]].sort()
        )
        assert client.get_weighted_avg_yield_to_maturity(ticker) is None
        assert client.get_merged_esg_as_of_dates(ticker) == 20220207
        assert (
            client.get_merged_esg_as_of_dates_formatted(ticker)
            == "Feb 07, 2022 (Dec 31, 2021)"
        )
        assert client.get_esg_suite_category(ticker) is None
        assert client.get_esg_suite_category_code(ticker) is None
        assert client.get_ter_ofc(ticker) is None
        assert client.get_model_oad_effective_duration(ticker) is None
        assert client.get_bid_price(ticker) is None


def test_get_product():
    client = Client()
    client.get_product("EFAV")
    # ToDo: Add some test logic here


def test_get_product_holdings():
    client = Client()
    client.get_holdings("EFAV")
    # ToDo: Add some test logic here
