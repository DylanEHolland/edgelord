from . import security_data

class security:
    data = None
    risk_free_rate = 0.02

    # Statistics
    #
    def changes(self, days = None, price_type = 'close'):
        return self.load_data(days, price_type).pct_change()

    def growth(self, days = None, price_type = 'close'):
        """Return percent growth for the given period"""
        data = self.load_data(days, price_type)
        
        # new - old / old = percent growth
        return (data.iloc[-1] - data.iloc[0]) / data.iloc[0]

    def sharpe(self, days = None, price_type = 'close'):
        """Return the equities sharpe ratio"""
        
        return (self.growth(days, price_type) - self.risk_free_rate) / self.standard_deviation(days, price_type)

    def standard_deviation(self, days = None, price_type = 'close'):
        return self.load_data(days, price_type).std()

    # Operations
    #
    def from_csv(self, file):
        """Build a security object from a CSV file"""

        self.data = security_data.security_data().from_csv(file)
        return self

    def load_data(self, days = None, price_type = 'close'):
        if days is None:
            days = len(self.data.frame().index)
        
        return self.data.frame()[price_type].tail(days)

    def risk_free(self, treasury_yield):
        """Set the risk free growth rate"""

        self.risk_free_rate = treasury_yield