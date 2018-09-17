class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        days = 1
        while self.stack and self.stack[-1][0] <= price:
            lastEntry = self.stack.pop()
            days += lastEntry[1]
        self.stack.append((price, days))
        return(days)