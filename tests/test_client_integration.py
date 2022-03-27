import pytest

from ishareslib.client import Client


@pytest.mark.integration
def test_column_names():
    client = Client()
    assert list(client.get_products()) == [
        "aladdinAssetClass",
        "aladdinAssetClassCode",
        "aladdinCountry",
        "aladdinCountryCode",
        "aladdinEsgClassification",
        "aladdinEsgClassificationCode",
        "aladdinMarketType",
        "aladdinMarketTypeCode",
        "aladdinRegion",
        "aladdinRegionCode",
        "aladdinSubAssetClass",
        "aladdinSubAssetClassCode",
        "cleanDuration",
        "cusip",
        "dailyPerformanceYearToDate",
        "effectiveDuration",
        "esgCoverage",
        "esgMsciQualityScore",
        "esgMsciQualityScoreAsOfDate",
        "esgRating",
        "esgReportHoldingAsOfDate",
        "fees",
        "fundName",
        "glsDoc",
        "inceptionDate",
        "investmentStyle",
        "investmentStyleCode",
        "investorClassName",
        "isin",
        "localExchangeTicker",
        "mgt",
        "modelOad",
        "navAmount",
        "navAmountAsOf",
        "navAnnualisedAsOf",
        "navFiveYearAnnualized",
        "navOneYearAnnualized",
        "navPerfAsOf",
        "navSinceInceptionAnnualized",
        "navTenYearAnnualized",
        "navThreeYearAnnualized",
        "navYearToDate",
        "netr",
        "optionAdjustedSpread",
        "optionAdjustedSpreadAsOf",
        "portfolioId",
        "priceFiveYearAnnualized",
        "priceOneYearAnnualized",
        "priceSinceInceptionAnnualized",
        "priceTenYearAnnualized",
        "priceThreeYearAnnualized",
        "priceYearAsOf",
        "priceYearToDate",
        "productPageUrl",
        "productView",
        "quarterlyNavAsOf",
        "quarterlyNavFiveYearAnnualized",
        "quarterlyNavOneYearAnnualized",
        "quarterlyNavSinceInceptionAnnualized",
        "quarterlyNavTenYearAnnualized",
        "quarterlyNavThreeYearAnnualized",
        "quarterlyNavYearToDate",
        "quarterlyPriceAsOf",
        "quarterlyPriceFiveYearAnnualized",
        "quarterlyPriceOneYearAnnualized",
        "quarterlyPriceSinceInceptionAnnualized",
        "quarterlyPriceTenYearAnnualized",
        "quarterlyPriceThreeYearAnnualized",
        "quarterlyPriceYearToDate",
        "sedol",
        "ter",
        "thirtyDaySecYield",
        "thirtyDaySecYieldAsOf",
        "totalNetAssets",
        "totalNetAssetsFund",
        "totalNetAssetsFundAsOf",
        "twelveMonTrlYield",
        "twelveMonTrlYieldAsOf",
        "unsubsidizedYield",
        "wtdAvgCarbonIntensity",
        "yieldToWorst",
        "yieldToWorstAsOf",
        "productRange",
        "productRangeCode",
        "weightedAvgYieldToMaturity",
        "mergedEsgAsOfDates",
        "esg.suiteCategory",
        "esg.suiteCategoryCode",
        "ter_ocf",
        "modelOad_effectiveDuration",
        "bidPrice",
        "esg.alternatives",
    ]


@pytest.mark.integration
def test_row_count():
    client = Client()
    assert client.get_products().shape[0] == 435