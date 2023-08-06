from numpy import indices
from tradingview_scraper import Ideas
from tradingview_scraper import Indicators

## TEST IDEAS CLASS
# a = Ideas().scraper(symbol = 'btc',
#                 wholePage = False,
#                 startPage = 1,
#                 endPage = 2, 
#                 to_csv = False,
#                 return_json=True)

# # print(a)
# print(a.keys())



## TEST INDICATORS CLASS
a = Indicators().scraper(
        exchange="BITSTAMP",
        symbols=["BTCUSD","LTCUSD"],
        indicators=["RSI","Stoch.K"],
        allIndicators=False
        )

print(a)