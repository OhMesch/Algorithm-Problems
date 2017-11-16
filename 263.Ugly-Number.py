'''
Problem:
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number. 
'''

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
        	return(True)
        if num == 0:
        	return(False)

        return(self.uglyHelper(num))

    def uglyHelper(self,num):
    	if num in [2,3,5]:
    		return(True)
    	if num % 2 == 0:
    		return(self.uglyHelper(num//2))
    	elif num % 3 == 0:
    		return(self.uglyHelper(num//3))
    	elif num % 5 == 0:
    		return(self.uglyHelper(num//5))
    	else:
    		return(False)

driver = Solution()
print('\n')

print("1")
print("**", driver.isUgly(1))
print("-- True\n")

print("2")
print("**", driver.isUgly(6))
print("-- True\n")

print("3")
print("**", driver.isUgly(8))
print("-- True\n")

print("4")
print("**", driver.isUgly(14))
print("-- False\n")