# Problem: Given an integer
# Return: Determine if the integer is a power of 2

class Solution(object):
	def isPowerOfTwo(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		strN = str(n)
		if strN[0] == '-':
			return(False)
		binary = list(format(n,'b'))
		if binary.count('1') == 1:
			return(True)
		else:
			return(False)

driver = Solution()

t1 = 5
t2 = 25
t3 = 2
t4 = 64
t5 = -16
print('\n')
print('Number',t1, '\nPower 2:',driver.isPowerOfTwo(t1),'\nExpected Answer:','False\n')
print('Number',t2, '\nPower 2:',driver.isPowerOfTwo(t2),'\nExpected Answer:','False\n')
print('Number',t3, '\nPower 2:',driver.isPowerOfTwo(t3),'\nExpected Answer:','True\n')
print('Number',t4, '\nPower 2:',driver.isPowerOfTwo(t4),'\nExpected Answer:','True\n')
print('Number',t5, '\nPower 2:',driver.isPowerOfTwo(t5),'\nExpected Answer:','False\n')