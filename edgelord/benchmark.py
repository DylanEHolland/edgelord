import numpy as np
from . import security as sc

class benchmark:
    """Benchmark stats for comparing one security to another"""
    security = None
    guage = None

    #
    #
    def __init__(self, security, benchmark_symbol):
        self.security = security
        self.guage = benchmark_symbol

    #
    #
    def beta(self, days = None, price_type = 'close'):
        data, guage = self.load_data(days, price_type)
        volatility = (data.std() / guage.std())
        result = self.correlation(days, price_type) * volatility

        return result

    #
    #
    def correlation(self, days = None, price_type = 'close'):
        """Return the correlation coeffecient between the two price arrays"""
        data, guage = self.load_data(days, price_type)
        
        return np.corrcoef(guage.values.tolist(), data.values.tolist())[0][1]

    #
    #
    def load_data(self, days = None, price_type = 'close'):
        """Load data for the time period"""
        
        if days is None:
            days = len(self.security.data.frame().index)
        
        return self.security.data.frame()[price_type].tail(days), self.guage.data.frame()[price_type].tail(days)