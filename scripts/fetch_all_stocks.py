import argparse
from datetime import datetime, date
import edgelord
from edgelord import FinancialModelingPrep as fmp
import os
import pandas
from tiingo import TiingoClient

def client():
    """Return an instance of TiingoClient"""

    return TiingoClient()

def fetch_profile(data):
    """Append price and market cap to data rows"""

    buffer = []
    count = 0
    total = len(data)

    for row in data:

        print(
            "%s%%" % (
                str( round( (count/total) * 100, 2 ) )
            )
        )

        try:
            tmp_data = fmp.company_profile(row['ticker'].replace("-", "."))
            row['market_cap'] = tmp_data['MktCap']
            row['price'] = tmp_data['Price']
            
            buffer.append(row)
        except KeyError:
            print("sigh")

        count += 1

    return buffer


def fetch_stocks(exchange = [], caps = False):
    """Return a list of all available stocks"""
    data_to_fetch = {'ticker': 'ticker', 'exchange': 'exchange', 'price_currency': 'priceCurrency', 'start_date': 'startDate', 'end_date': 'endDate'}

    result_list = []
    print("Fetching list...", end=' ')
    count = 0
    for equity in client().list_stock_tickers():
        if count == 0:
            print("Done.")

        last_date = equity['endDate'].split("-")
        run = True
        try:
            last_date = datetime(year=int(last_date[0]), month=int(last_date[1]), day=int(last_date[2]))
            if last_date < edgelord.previous_business_day(1):
                run = False
        
        except ValueError:
            run = False
        
        if run:
            run = False
            for ex in exchange:
                if ex is not '' and len(exchange) > 0 and equity['exchange'].lower() == ex.lower():
                    run = True

            if run:
                buffer = {}
                for index in data_to_fetch:
                    buffer[index] = equity[data_to_fetch[index]]
                
                result_list.append(buffer)

        count += 1

    if caps:
        result_list = fetch_profile(result_list)

    return pandas.DataFrame(result_list)

def fetch_args():
    buffer = argparse.ArgumentParser()
    buffer.add_argument("-c", "--caps", help="Pull market caps as well", action="store_true")
    buffer.add_argument("-e", "--exchange", help="Exchange (of list of exchanges seperated by ,)", required=False)
    buffer.add_argument("-f", "--filename", help="Filename to write to", required=False)
    buffer.add_argument("-w", "--write", help="Write to disk", action="store_true")
    return buffer.parse_args()

if __name__ == "__main__":
    arguments = fetch_args()
    exchanges = arguments.exchange.split(",")

    data = fetch_stocks(exchange = exchanges, caps = arguments.caps)
    if arguments.write:
        filename = "%s/.stock_list.json" % (os.environ['HOME'])
        if arguments.filename:
            filename = arguments.filename

        data.to_json(filename, orient='split')
    else:
        print(data)