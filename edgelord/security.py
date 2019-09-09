from . import security_data
from . import benchmark as bm

class security:
    data = None
    risk_free_rate = 0.02

    #   Compare against another equity
    #
    def benchmark(self, foreign_symbol):
        """Return a benchmark class with this security and the benchmark"""
        return bm.benchmark(self, foreign_symbol)

    # Statistics
    #
    def changes(self, days = None, price_type = 'close'):
        """Daily changes in price"""

        return self.load_data(days, price_type).pct_change()

    # 
    #
    def growth(self, days = None, price_type = 'close'):
        """Return percent growth for the given period"""

        data = self.load_data(days, price_type)
        
        # (new - old) / old = percent growth
        return (data.iloc[-1] - data.iloc[0]) / data.iloc[0]

    #
    #
    def price(self, days = None, price_type = 'close'):
        data = self.load_data(days, price_type)

        if days is None:
            data = data.tail(1).iloc[0]
        else:
            data = data.values.tolist()

        return data

    #
    #
    def sharpe(self, days = None, price_type = 'close'):
        """Return the equities sharpe ratio"""
        
        return (self.growth(days, price_type) - self.risk_free_rate) / self.standard_deviation(days, price_type)

    #  
    #
    def simple_moving_average(self, days = None, price_type = 'close'):
        """Return the simple moving average"""

        data = self.load_data(days, price_type).mean()
        print(data)

    def standard_deviation(self, days = None, price_type = 'close'):
        return self.load_data(days, price_type).std()

    #
    #
    def volume(self, days = None, sum = False):
        """Return the volume (or average volume) for the given amount of days"""
        data = self.load_data(days)

        if days is None:
            data = data.tail(1).iloc[0]
        else:
            if sum:
                data = data.mean()
            else:
                data = data.values.tolist()

        return data

    # Operations
    #
    def from_csv(self, file):
        """Build a security object from a CSV file"""

        self.data = security_data.security_data().from_csv(file)
        return self

    #
    #
    def load_data(self, days = None, price_type = 'close'):
        """Load data for the time period"""

        if days is None:
            days = len(self.data.frame().index)
        
        return self.data.frame()[price_type].tail(days)

    #
    #
    def risk_free(self, treasury_yield):
        """Set the risk free growth rate"""

        self.risk_free_rate = treasury_yield