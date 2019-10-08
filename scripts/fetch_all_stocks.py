import lsequity
import os
from tiingo import TiingoClient

def client():
    """Return an instance of TiingoClient"""

    return TiingoClient()

def fetch_stocks():
    """Return a list of all available stocks"""
    data_to_fetch = {'ticker': 'ticker', 'exchange': 'exchange', 'price_currency': 'priceCurrency', 'start_date': 'startDate', 'end_date': 'endDate'}

    result_list = []
    for equity in client().list_stock_tickers():
        buffer = {}
        for index in data_to_fetch:
            buffer[index] = equity[data_to_fetch[index]]
        
        result_list.append(buffer)

    return result_list

def update():
    """Update stock list"""

    print("Updating stocks...\nFetching list...", end=' ')
    stocks = fetch_stocks()
    print("Done.")

    pandas.DataFrame(stocks).to_json("%s/.stock_list.json" % (os.environ['HOME']))

if __name__ == "__main__":
    lsequity.update()