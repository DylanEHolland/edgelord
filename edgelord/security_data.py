from datetime import datetime
import pandas
from pandas.tseries.offsets import BDay
from tiingo import TiingoClient

def last_business_day(days = 1):
    """Return the date for the last business day"""

    today = pandas.datetime.today()
    today = str(today - BDay(days)).split(" ")[0].split("-")
    today = datetime(int(today[0]), int(today[1]), int(today[2]))

    return today

class security_data:
    """Time series data"""
    columns_allowed = None
    data = None

    # Magic subroutines
    #
    def __init__(self):
        self.columns_allowed = ['close', 'high', 'low', 'open', 'volume']

    def __str__(self):
        return str(self.frame())

    # Operation subroutines
    #
    def build(self, data):
        """Restructure data to be usable"""

        self.data = []
        
        for row in data.values.tolist():
            self.data.append(row)

        self.columns = data.columns
        return self

    def frame(self):
        """Return data as dataframe"""

        return pandas.DataFrame(self.data, columns = self.columns).sort_values(by=['date'])

    def from_csv(self, file):
        """Build a security_data object from the given CSV file"""
        
        data = pandas.read_csv(file)
        return self.build(data)


    def from_json(self, file):
        """Build a security_data object from the given JSON file"""

        with open(file, 'r') as f:
            data = f.read()
            f.close()
        
        data = pandas.read_json(data)
        data = data.sort_values(by=['date'])
        return self.build(data)

    def from_rest(self, ticker):
        """Download data from Tiingo"""

        client = TiingoClient()
        data = client.get_ticker_price(ticker, startDate=last_business_day(300), endDate=last_business_day())

        result = []

        column_list = None
        set_columns = False
        for row in data:
            buffer = {}
            
            if column_list is None and not set_columns:
                column_list = []

            for column in row:
                # Loop through each rows column list
                if ("adj" in column) or (column == 'date'):
                    # Only grab adjusted data (to account for any splits)

                    column_name = column.replace("adj", "").lower()

                    if not set_columns:
                        column_list.append(column.replace("adj", "").lower())

                    if column == 'date':
                        buffer[column_name] = row[column].split("T")[0]
                    else:
                        buffer[column_name] = row[column]

            if not set_columns and column_list is not None:
                # Only set the column list once
                set_columns = True

            result.append(buffer)

        data = pandas.DataFrame(result, columns=column_list)
        data = data.sort_values(by=['date'])
        return self.build(data)
        