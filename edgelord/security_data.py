import pandas

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

    # Getter Subroutines
    #
    def frame(self):
        """Return data as dataframe"""

        return pandas.DataFrame(self.data, columns = self.columns)

    # Operation subroutines
    #
    def build(self, data):
        self.data = []
        
        for row in data.values.tolist():
            self.data.append(row)

        self.columns = data.columns
        return self

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
