# Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k, whether a Fibonacci number could be used multiple times.

# It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum k. 

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_seq = self.generateFibUnil(k)
        zero_count = 0
        for i in range(len(fib_seq) -1, -1, -1):
            while k > fib_seq[i]:
                k -= fib_seq[i]
                zero_count += 1
            if k == fib_seq[i]:
                zero_count += 1
                return zero_count
        
    def generateFibUnil(self, k: int) -> int:
        fib = [1, 1]
        counter = 2
        while(fib[-1] < k):
            fib.append(fib[counter-1] + fib[counter-2])
            counter += 1
        return fib