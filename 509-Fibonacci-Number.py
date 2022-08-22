class Solution:
    def fib(self, n: int) -> int:
        fib_seq = [0 for i in range(n)]
        fib_seq[1] = 1
        
        for i in range(2, n):
            fib_seq[i] = fib_seq[i-2]+fib_seq[i-1]
        
        return fib_seq[n-1]+fib_seq[n-2]