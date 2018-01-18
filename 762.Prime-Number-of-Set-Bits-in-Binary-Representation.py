# Problem:
# Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

# (Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.) 

# Note:

#     L, R will be integers L <= R in the range [1, 10^6].
#     R - L will be at most 10000.


class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        sol = 0

        # We don't care about any primes over 19 as R can be as 2^20 > 1e6 and 20 isn't prime
        primes = {2,3,5,7,11,13,17,19}
        
        ones = [("{0:b}".format(x)).count('1') for x in range(L,R+1)]
        
        for elm in ones:
            if elm in primes:
                sol+=1

        return(sol)


driver = Solution()

print('\n1')
print('**', driver.countPrimeSetBits(6,10))
print('-- 4\n')

print('2')
print('**', driver.countPrimeSetBits(10,15))
print('-- 5\n')

print('3')
print('**', driver.countPrimeSetBits(1,10000))
print('-- 4252\n')

print('4')
print('**', driver.countPrimeSetBits(990000,1000000))
print('-- 3754\n')

print('5')
print('**', driver.countPrimeSetBits(1,2))
print('-- 0\n')