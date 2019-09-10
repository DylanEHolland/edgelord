class indicators:
    def __init__(self, security):
        self.security = security

    def daily_dips(self, days = None, amount = 0.05):
        """Return the number of $amount (or greater) sized dips in the number of $days"""
        
        total_dips = 0
        data = self.security.load_data(days).values.tolist()
        for n in range(len(data)):

            day = data[n]
            yesterday = data[n - 1]

            if day < yesterday:
                if (yesterday - day) / yesterday >= amount:
                    total_dips += 1

        return total_dips

    def largest_drawdown(self, days = None):
        """Return the largest dip amount"""

        largest = 0
        drawdown = 0
        price_at_start = 0
        data = self.security.load_data(days).values.tolist()
        for n in range(len(data)):
            day = data[n]
            yesterday = data[n - 1]

            if day < yesterday:
                if drawdown is 0:
                    price_at_start = day

                drawdown += yesterday - day
            else:
                if drawdown > 0:
                    if drawdown > largest:
                        largest = drawdown

                    drawdown = 0

        return largest