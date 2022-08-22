class Solution:
    def fib(self, n: int) -> int:
        if n!=0:
            fib_seq = [0 for _ in range(n+1)]
            fib_seq[1] = 1
            
            for i in range(2, n+1):
                fib_seq[i] = fib_seq[i-2]+fib_seq[i-1]
            
            return fib_seq[n]
        else:
            return 0