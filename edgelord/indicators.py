class indicators:
    def __init__(self, security):
        self.security = security

    def dips(self, amount = 0.05, days = None):
        """Return the number of $amount (or greater) sized dips in the number of $days"""

        raise NotImplementedError

    