"""Generate a dataset (json or csv) from the Tiingo api"""

# You must set the $TIINGO_API_KEY environment variable
from argparse import ArgumentParser
from datetime import datetime
from tiingo import TiingoClient
import pandas
from pandas.tseries.offsets import BDay

def last_business_day(days = 1):
    """Return the date for the last business day"""

    today = pandas.datetime.today()
    today = str(today - BDay(days)).split(" ")[0].split("-")
    today = datetime(int(today[0]), int(today[1]), int(today[2]))

    return today

def load_data(ticker):
    """Return data for the given ticker symbol"""

    client = TiingoClient()
    data = client.get_ticker_price(ticker, startDate=last_business_day(253), endDate=last_business_day())

    result = []

    column_list = None
    set_columns = False
    for row in data:
        buffer = {}
        
        if column_list is None and not set_columns:
            column_list = []

        for column in row:
            # Loop through each rows column list
            if "adj" in column:
                # Only grab adjusted data (to account for any splits)

                column_name = column.replace("adj", "").lower()

                if not set_columns:
                    column_list.append(column.replace("adj", "").lower())

                buffer[column_name] = row[column]

        if not set_columns and column_list is not None:
            # Only set the column list once
            set_columns = True

        result.append(buffer)

    return pandas.DataFrame(result, columns=column_list)

if __name__ == "__main__":

    ap = ArgumentParser()
    ap.add_argument('-f', '--output-file', help="The CSV file to output to", required=True)
    ap.add_argument('-t', '--ticker-symbol', help="The ticker to load data for", required=True)
    ap = ap.parse_args()

    load_data(ap.ticker_symbol).to_csv(ap.output_file)