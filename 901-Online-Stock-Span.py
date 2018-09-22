'''
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.
The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
'''

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
        
driver = StockSpanner()
sol = [None]
sol.append(driver.next(100))
sol.append(driver.next(80))
sol.append(driver.next(60))
sol.append(driver.next(70))
sol.append(driver.next(60))
sol.append(driver.next(75))
sol.append(driver.next(85))
print(sol)
print([None,1,1,1,2,1,4,6])

print("\n")
driver = StockSpanner()
sol = [None]
sol.append(driver.next(10))
sol.append(driver.next(20))
sol.append(driver.next(30))
sol.append(driver.next(40))
print(sol)
print([None,1,2,3,4])

print("\n")
driver = StockSpanner()
sol = [None]
sol.append(driver.next(40))
sol.append(driver.next(30))
sol.append(driver.next(20))
sol.append(driver.next(10))
print(sol)
print([None,1,1,1,1])