import pandas

class security_data:
    """Time series data"""
    columns_allowed = None
    data = None

    def __init__(self):
        self.columns_allowed = ['close', 'high', 'low', 'open', 'volume']

    def __str__(self):
        return str(self.dataframe())

    def dataframe(self):
        """Return data as dataframe"""
        return pandas.DataFrame(self.data, columns = self.columns)

    def from_csv(self, file):
        """Build a security_data object from the given CSV file"""
        
        data = pandas.read_csv(file)

        self.data = []
        
        for row in data.values.tolist():
            self.data.append(row)

        self.columns = data.columns

        return self