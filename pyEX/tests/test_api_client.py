# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

import pyEX as p


class TestPyEXClientAPI:
    def setup(self):
        self.c = p.Client("pk_123")

    def test_all_rules(self):

        for meth in (
            "schema",
            "rules",
            "createRule",
            "lookupRule",
            "pauseRule",
            "resumeRule",
            "deleteRule",
            "ruleInfo",
            "ruleOutput",
        ):
            assert hasattr(self.c, meth)
            # assert hasattr(self.c.rules, meth)

    def test_all_refdata(self):
        for meth in (
            "symbols",
            "iexSymbols",
            "mutualFundSymbols",
            "otcSymbols",
            "internationalSymbols",
            "fxSymbols",
            "optionsSymbols",
            "cryptoSymbols",
            "futuresSymbols",
            "symbolsDF",
            "iexSymbolsDF",
            "mutualFundSymbolsDF",
            "otcSymbolsDF",
            "internationalSymbolsDF",
            "fxSymbolsDF",
            "optionsSymbolsDF",
            "cryptoSymbolsDF",
            "futuresSymbolsDF",
            "symbolsList",
            "iexSymbolsList",
            "mutualFundSymbolsList",
            "otcSymbolsList",
            "internationalSymbolsList",
            "fxSymbolsList",
            "optionsSymbolsList",
            "cryptoSymbolsList",
            "futuresSymbolsList",
            "isinLookup",
            "isinLookupDF",
            "ricLookup",
            "ricLookupDF",
            "corporateActions",
            "corporateActionsDF",
            "refDividends",
            "refDividendsDF",
            "nextDayExtDate",
            "nextDayExtDateDF",
            "directory",
            "directoryDF",
            "calendar",
            "calendarDF",
            "holidays",
            "holidaysDF",
            "exchanges",
            "exchangesDF",
            "figi",
            "figiDF",
            "internationalExchanges",
            "internationalExchangesDF",
            "sectors",
            "sectorsDF",
            "search",
            "searchDF",
            "tags",
            "tagsDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.refdata, meth)

    def test_all_markets(self):
        for meth in (
            "markets",
            "marketsDF",
            "marketVolume",
            "marketVolumeDF",
            "marketShortInterest",
            "marketShortInterestDF",
            "marketNews",
            "marketNewsDF",
            "marketOhlc",
            "marketOhlcDF",
            "marketPrevious",
            "marketPreviousDF",
            "marketYesterday",
            "marketYesterdayDF",
            "sectorPerformance",
            "sectorPerformanceDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.market, meth)

    def test_all_metadata(self):
        for meth in (
            "queryMetadata",
            "queryMetadataDF",
        ):
            assert hasattr(self.c, meth)

    def test_all_stats(self):
        for meth in (
            "systemStats",
            "systemStatsDF",
            "recent",
            "recentDF",
            "records",
            "recordsDF",
            "summary",
            "summaryDF",
            "daily",
            "dailyDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.stats, meth)

    def test_all_ts(self):
        for meth in (
            "timeSeriesInventory",
            "timeSeriesInventoryDF",
            "timeSeries",
            "timeSeriesDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c, meth)

    def test_all_stock(self):
        for meth in (
            "advancedStats",
            "advancedStatsDF",
            "analystRecommendations",
            "analystRecommendationsDF",
            "balanceSheet",
            "balanceSheetDF",
            "batch",
            "batchDF",
            "bonusIssue",
            "bonusIssueDF",
            "bulkBatch",
            "bulkBatchDF",
            "book",
            "bookDF",
            "cashFlow",
            "cashFlowDF",
            "chart",
            "chartDF",
            "bulkMinuteBars",
            "bulkMinuteBarsDF",
            "company",
            "companyDF",
            "collections",
            "collectionsDF",
            "delayedQuote",
            "delayedQuoteDF",
            "distribution",
            "distributionDF",
            "dividends",
            "dividendsBasic",
            "dividendsDF",
            "dividendsBasicDF",
            "earnings",
            "earningsDF",
            "earningsToday",
            "earningsTodayDF",
            "spread",
            "spreadDF",
            "financials",
            "financialsDF",
            "fortyF",
            "fundOwnership",
            "fundOwnershipDF",
            "fundamentals",
            "fundamentalsDF",
            "incomeStatement",
            "incomeStatementDF",
            "insiderRoster",
            "insiderRosterDF",
            "insiderSummary",
            "insiderSummaryDF",
            "insiderTransactions",
            "insiderTransactionsDF",
            "institutionalOwnership",
            "institutionalOwnershipDF",
            "intraday",
            "intradayDF",
            "ipoToday",
            "ipoTodayDF",
            "ipoUpcoming",
            "ipoUpcomingDF",
            "threshold",
            "thresholdDF",
            "shortInterest",
            "shortInterestDF",
            "estimates",
            "estimatesDF",
            "keyStats",
            "keyStatsDF",
            "largestTrades",
            "largestTradesDF",
            "list",
            "listDF",
            "logo",
            "logoPNG",
            "logoNotebook",
            "news",
            "newsDF",
            "ohlc",
            "ohlcDF",
            "optionExpirations",
            "options",
            "optionsDF",
            "peers",
            "peersDF",
            "previous",
            "previousDF",
            "yesterday",
            "yesterdayDF",
            "price",
            "priceDF",
            "priceTarget",
            "priceTargetDF",
            "quote",
            "quoteDF",
            "relevant",
            "relevantDF",
            "returnOfCapital",
            "returnOfCapitalDF",
            "rightsIssue",
            "rightsIssueDF",
            "rightToPurchase",
            "rightToPurchaseDF",
            "securityReclassification",
            "securityReclassificationDF",
            "securitySwap",
            "securitySwapDF",
            "spinoff",
            "spinoffDF",
            "splits",
            "splitsDF",
            "stockSplits",
            "stockSplitsDF",
            "tenQ",
            "tenK",
            "technicals",
            "technicalsDF",
            "twentyF",
            "upcomingEvents",
            "upcomingEventsDF",
            "upcomingEarnings",
            "upcomingEarningsDF",
            "upcomingDividends",
            "upcomingDividendsDF",
            "upcomingSplits",
            "upcomingSplitsDF",
            "upcomingIPOs",
            "upcomingIPOsDF",
            "volumeByVenue",
            "volumeByVenueDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.stocks, meth)

    def test_all_iex(self):
        for meth in (
            "iexAuction",
            "iexAuctionAsync",
            "iexAuctionDF",
            "iexBook",
            "iexBookAsync",
            "iexBookDF",
            "iexDeep",
            "iexDeepAsync",
            "iexDeepDF",
            "iexHist",
            "iexHistAsync",
            "iexHistDF",
            "iexLast",
            "iexLastAsync",
            "iexLastDF",
            "iexOfficialPrice",
            "iexOfficialPriceAsync",
            "iexOfficialPriceDF",
            "iexOpHaltStatus",
            "iexOpHaltStatusAsync",
            "iexOpHaltStatusDF",
            "iexSecurityEvent",
            "iexSecurityEventAsync",
            "iexSecurityEventDF",
            "iexSsrStatus",
            "iexSsrStatusAsync",
            "iexSsrStatusDF",
            "iexSystemEvent",
            "iexSystemEventAsync",
            "iexSystemEventDF",
            "iexTops",
            "iexTopsAsync",
            "iexTopsDF",
            "iexTradeBreak",
            "iexTradeBreakAsync",
            "iexTradeBreakDF",
            "iexTrades",
            "iexTradesAsync",
            "iexTradesDF",
            "iexTradingStatus",
            "iexTradingStatusAsync",
            "iexTradingStatusDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.iex, meth)

    def test_all_streaming(self):
        for meth in (
            "topsSSE",
            "topsSSEAsync",
            "lastSSE",
            "lastSSEAsync",
            "deepSSE",
            "deepSSEAsync",
            "tradesSSE",
            "tradesSSEAsync",
            "stocksUSNoUTPSSE",
            "stocksUSNoUTPSSEAsync",
            "stocksUSSSE",
            "stocksUSSSEAsync",
            "stocksUS1SecondSSE",
            "stocksUSNoUTP1SecondSSE",
            "stocksUS1SecondSSEAsync",
            "stocksUSNoUTP1SecondSSEAsync",
            "stocksUS5SecondSSE",
            "stocksUSNoUTP5SecondSSE",
            "stocksUS5SecondSSEAsync",
            "stocksUSNoUTP5SecondSSEAsync",
            "stocksUS1MinuteSSE",
            "stocksUSNoUTP1MinuteSSE",
            "stocksUS1MinuteSSEAsync",
            "stocksUSNoUTP1MinuteSSEAsync",
            "fxSSE",
            "fxSSEAsync",
            "forex1SecondSSE",
            "forex1SecondSSEAsync",
            "forex5SecondSSE",
            "forex5SecondSSEAsync",
            "forex1MinuteSSE",
            "forex1MinuteSSEAsync",
            "newsSSE",
            "newsSSEAsync",
            "sentimentSSE",
            "sentimentSSEAsync",
            "cryptoBookSSE",
            "cryptoBookSSEAsync",
            "cryptoEventsSSE",
            "cryptoEventsSSEAsync",
            "cryptoQuotesSSE",
            "cryptoQuotesSSEAsync",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.streaming, meth)

    def test_all_account(self):
        for meth in (
            "messageBudget",
            "metadata",
            "metadataDF",
            "usage",
            "usageDF",
        ):
            assert hasattr(self.c, meth)
            # assert hasattr(self.c.account, meth)

    def test_all_alternative(self):
        for meth in (
            "sentiment",
            "sentimentDF",
            "ceoCompensation",
            "ceoCompensationDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.alternative, meth)

    def test_all_points(self):
        for meth in ("points", "pointsDF"):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.points, meth)

    def test_all_fx(self):
        for meth in (
            "latestFX",
            "latestFXDF",
            "convertFX",
            "convertFXDF",
            "historicalFX",
            "historicalFXDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.fx, meth)

    def test_all_crypto(self):
        for meth in (
            "cryptoBook",
            "cryptoBookDF",
            "cryptoQuote",
            "cryptoQuoteDF",
            "cryptoPrice",
            "cryptoPriceDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.crypto, meth)

    def test_all_files(self):
        for meth in ("file", "download"):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.files, meth)

    def test_all_premium(self):
        for meth in (
            "analystDays",
            "analystDaysDF",
            "boardOfDirectorsMeeting",
            "boardOfDirectorsMeetingDF",
            "businessUpdates",
            "businessUpdatesDF",
            "buybacks",
            "buybacksDF",
            "capitalMarketsDay",
            "capitalMarketsDayDF",
            "companyTravel",
            "companyTravelDF",
            "filingDueDates",
            "filingDueDatesDF",
            "fiscalQuarterEnd",
            "fiscalQuarterEndDF",
            "forum",
            "forumDF",
            "generalConference",
            "generalConferenceDF",
            "fdaAdvisoryCommitteeMeetings",
            "fdaAdvisoryCommitteeMeetingsDF",
            "holidays",
            "holidaysDF",
            "indexChanges",
            "indexChangesDF",
            "ipos",
            "iposDF",
            "legalActions",
            "legalActionsDF",
            "mergersAndAcquisitions",
            "mergersAndAcquisitionsDF",
            "productEvents",
            "productEventsDF",
            "researchAndDevelopmentDays",
            "researchAndDevelopmentDaysDF",
            "sameStoreSales",
            "sameStoreSalesDF",
            "secondaryOfferings",
            "secondaryOfferingsDF",
            "seminars",
            "seminarsDF",
            "shareholderMeetings",
            "shareholderMeetingsDF",
            "summitMeetings",
            "summitMeetingsDF",
            "tradeShows",
            "tradeShowsDF",
            "witchingHours",
            "witchingHoursDF",
            "workshops",
            "workshopsDF",
            "nonTimelyFilings",
            "nonTimelyFilingsDF",
            "similarityIndex",
            "similarityIndexDF",
            "cam1",
            "cam1DF",
            "esgCFPBComplaints",
            "esgCFPBComplaintsDF",
            "esgCPSCRecalls",
            "esgCPSCRecallsDF",
            "esgDOLVisaApplications",
            "esgDOLVisaApplicationsDF",
            "esgEPAEnforcements",
            "esgEPAEnforcementsDF",
            "esgEPAMilestones",
            "esgEPAMilestonesDF",
            "esgFECIndividualCampaingContributions",
            "esgFECIndividualCampaingContributionsDF",
            "esgOSHAInspections",
            "esgOSHAInspectionsDF",
            "esgSenateLobbying",
            "esgSenateLobbyingDF",
            "esgUSASpending",
            "esgUSASpendingDF",
            "esgUSPTOPatentApplications",
            "esgUSPTOPatentApplicationsDF",
            "esgUSPTOPatentGrants",
            "esgUSPTOPatentGrantsDF",
            "tacticalModel1",
            "tacticalModel1DF",
            "precisionAlphaPriceDynamics",
            "precisionAlphaPriceDynamicsDF",
            "thirtyDaySentiment",
            "thirtyDaySentimentDF",
            "sevenDaySentiment",
            "sevenDaySentimentDF",
            "twentyOneDayMLReturnRanking",
            "twentyOneDayMLReturnRankingDF",
            "tenDayMLReturnRanking",
            "tenDayMLReturnRankingDF",
            "fiveDayMLReturnRanking",
            "fiveDayMLReturnRankingDF",
            "threeDayMLReturnRanking",
            "threeDayMLReturnRankingDF",
            "twoDayMLReturnRanking",
            "twoDayMLReturnRankingDF",
            "languageMetricsOnCompanyFilingsAll",
            "languageMetricsOnCompanyFilingsAllDF",
            "languageMetricsOnCompanyFilings",
            "languageMetricsOnCompanyFilingsDF",
            "languageMetricsOnCompanyFilingsDifferenceAll",
            "languageMetricsOnCompanyFilingsDifferenceAllDF",
            "languageMetricsOnCompanyFilingsDifference",
            "languageMetricsOnCompanyFilingsDifferenceDF",
            "kScore",
            "kScoreDF",
            "kScoreChina",
            "kScoreChinaDF",
            "accountingQualityAndRiskMatrix",
            "accountingQualityAndRiskMatrixDF",
            "directorAndOfficerChanges",
            "directorAndOfficerChangesDF",
        ):
            assert hasattr(self.c.premium, meth)

    def test_all_files_premium(self):
        for meth in (
            "valuEngine",
            "valuEngineDownload",
            "newConstructs",
            "newConstructsDownload",
        ):
            assert hasattr(self.c.premium.files, meth)

    def test_all_treasuries(self):
        for meth in (
            "thirtyYear",
            "twentyYear",
            "tenYear",
            "sevenYear",
            "fiveYear",
            "threeYear",
            "twoYear",
            "oneYear",
            "sixMonth",
            "threeMonth",
            "oneMonth",
            "thirtyYearHistory",
            "thirtyYearHistoryDF",
            "twentyYearHistory",
            "twentyYearHistoryDF",
            "tenYearHistory",
            "tenYearHistoryDF",
            "sevenYearHistory",
            "sevenYearHistoryDF",
            "fiveYearHistory",
            "fiveYearHistoryDF",
            "threeYearHistory",
            "threeYearHistoryDF",
            "twoYearHistory",
            "twoYearHistoryDF",
            "oneYearHistory",
            "oneYearHistoryDF",
            "sixMonthHistory",
            "sixMonthHistoryDF",
            "threeMonthHistory",
            "threeMonthHistoryDF",
            "oneMonthHistory",
            "oneMonthHistoryDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.rates, meth)

    def test_all_commods(self):
        for meth in (
            "wti",
            "brent",
            "natgas",
            "heatoil",
            "jet",
            "diesel",
            "gasreg",
            "gasmid",
            "gasprm",
            "propane",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.commodities, meth)

    def test_all_rates(self):
        for meth in (
            "us30",
            "us15",
            "us5",
            "fedfunds",
            "creditcard",
            "cdnj",
            "cdj",
            "gdp",
            "indpro",
            "cpi",
            "payroll",
            "housing",
            "unemployment",
            "vehicles",
            "recessionProb",
            "initialClaims",
            "institutionalMoney",
            "retailMoney",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.economic, meth)

    def test_all_studies(self):
        for meth in (
            "peerCorrelation",
            "peerCorrelationPlot",
            "yieldCurve",
            "returns",
            "dailyReturns",
            "ht_dcperiod",
            "ht_dcphase",
            "ht_phasor",
            "ht_sine",
            "ht_trendmode",
            "acos",
            "asin",
            "atan",
            "ceil",
            "cos",
            "cosh",
            "exp",
            "floor",
            "ln",
            "log10",
            "sin",
            "sinh",
            "sqrt",
            "tan",
            "tanh",
            "add",
            "div",
            "max",
            "maxindex",
            "min",
            "minindex",
            "minmax",
            "minmaxindex",
            "mult",
            "sub",
            "sum",
            "adx",
            "adxr",
            "apo",
            "aroon",
            "aroonosc",
            "bop",
            "cci",
            "cmo",
            "dx",
            "macd",
            "macdext",
            "mfi",
            "minus_di",
            "minus_dm",
            "mom",
            "plus_di",
            "plus_dm",
            "ppo",
            "roc",
            "rocp",
            "rocr",
            "rocr100",
            "rsi",
            "stoch",
            "stochf",
            "stochrsi",
            "trix",
            "ultosc",
            "willr",
            "bollinger",
            "dema",
            "ema",
            "ht_trendline",
            "kama",
            "mama",
            "mavp",
            "midpoint",
            "midpice",
            "sar",
            "sarext",
            "sma",
            "t3",
            "tema",
            "trima",
            "wma",
            "cdl2crows",
            "cdl3blackcrows",
            "cdl3inside",
            "cdl3linestrike",
            "cdl3outside",
            "cdl3starsinsouth",
            "cdl3whitesoldiers",
            "cdlabandonedbaby",
            "cdladvanceblock",
            "cdlbelthold",
            "cdlbreakaway",
            "cdlclosingmarubozu",
            "cdlconcealbabyswallow",
            "cdlcounterattack",
            "cdldarkcloudcover",
            "cdldoji",
            "cdldojistar",
            "cdldragonflydoji",
            "cdlengulfing",
            "cdleveningdojistar",
            "cdleveningstar",
            "cdlgapsidesidewhite",
            "cdlgravestonedoji",
            "cdlhammer",
            "cdlhangingman",
            "cdlharami",
            "cdlharamicross",
            "cdlhighwave",
            "cdlhikkake",
            "cdlhikkakemod",
            "cdlhomingpigeon",
            "cdlidentical3crows",
            "cdlinneck",
            "cdlinvertedhammer",
            "cdlkicking",
            "cdlkickingbylength",
            "cdlladderbottom",
            "cdllongleggeddoji",
            "cdllongline",
            "cdlmarubozu",
            "cdlmatchinglow",
            "cdlmathold",
            "cdlmorningdojistar",
            "cdlmorningstar",
            "cdlonneck",
            "cdlpiercing",
            "cdlrickshawman",
            "cdlrisefall3methods",
            "cdlseparatinglines",
            "cdlshootingstar",
            "cdlshortline",
            "cdlspinningtop",
            "cdlstalledpattern",
            "cdlsticksandwich",
            "cdltakuri",
            "cdltasukigap",
            "cdlthrusting",
            "cdltristar",
            "cdlunique3river",
            "cdlxsidegap3methods",
            "avgprice",
            "medprice",
            "typprice",
            "wclprice",
            "beta",
            "correl",
            "linearreg",
            "linearreg_angle",
            "linearreg_intercept",
            "linearreg_slope",
            "stddev",
            "tsf",
            "var",
            "atr",
            "natr",
            "trange",
            "ad",
            "adosc",
            "obv",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.studies, meth)
