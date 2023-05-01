TRAIN_START_DATE = "2019-01-07"  # bug fix: start on Monday
TRAIN_END_DATE = "2019-2-07"

TEST_START_DATE = "2022-01-03"
TEST_END_DATE = "2022-02-03"

TRADE_START_DATE = "2023-01-02"
TRADE_END_DATE = "2023-03-24"

# stockstats technical indicator column names
# check https://pypi.org/project/stockstats/ for different names
INDICATORS = [
    "vwma",
    "atr",
    "macd",
    "boll_ub",
    "boll_lb",
    "rsi",
    "cci",
    "mfi",
    "dx",
    "wt1",
    "wt2",
    "kdjk",
    "kdjd",
    "kdjj",
    "supertrend",
    "tema",
]

CDL = [
    "CDLDOJI",
    "CDLDRAGONFLYDOJI",
    "CDLGRAVESTONEDOJI",
    "CDLENGULFING",
    "CDLHAMMER",
    "CDLHANGINGMAN",
    "CDLHARAMI",
    "CDLHARAMICROSS",
    "CDLINVERTEDHAMMER",
    "CDLLONGLEGGEDDOJI",
    "CDLMORNINGDOJISTAR",
    "CDLMORNINGSTAR",
    "CDLEVENINGDOJISTAR",
    "CDLEVENINGSTAR",
    "CDLPIERCING",
    "CDLSHOOTINGSTAR",
    "CDLSPINNINGTOP",
]

# Possible time zones
TIME_ZONE_SHANGHAI = "Asia/Shanghai"  # Hang Seng HSI, SSE, CSI
TIME_ZONE_USEASTERN = "US/Eastern"  # Dow, Nasdaq, SP
TIME_ZONE_PARIS = "Europe/Paris"  # CAC,
TIME_ZONE_BERLIN = "Europe/Berlin"  # DAX, TECDAX, MDAX, SDAX
TIME_ZONE_JAKARTA = "Asia/Jakarta"  # LQ45
TIME_ZONE_SELFDEFINED = "xxx"  # If neither of the above is your time zone, you should define it, and set USE_TIME_ZONE_SELFDEFINED 1.
USE_TIME_ZONE_SELFDEFINED = 0  # 0 (default) or 1 (use the self defined)

# parameters for data sources
ALPACA_API_KEY = "xxx"  # your ALPACA_API_KEY
ALPACA_API_SECRET = "xxx"  # your ALPACA_API_SECRET
ALPACA_API_BASE_URL = "https://paper-api.alpaca.markets"  # alpaca url
