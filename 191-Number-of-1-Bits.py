# Problem: Given an integer
# Return: Return the Hamming weight

class Solution(object):
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return((list(format(n,'b'))).count('1'))

driver = Solution()

t1 = 5
t2 = 25
t3 = 2
t4 = 64
t5 = -16
print('\n')
print('Number',t1, '\nPower 2:',driver.hammingWeight(t1),'\nExpected Answer:','False\n')
print('Number',t2, '\nPower 2:',driver.hammingWeight(t2),'\nExpected Answer:','False\n')
print('Number',t3, '\nPower 2:',driver.hammingWeight(t3),'\nExpected Answer:','True\n')
print('Number',t4, '\nPower 2:',driver.hammingWeight(t4),'\nExpected Answer:','True\n')
print('Number',t5, '\nPower 2:',driver.hammingWeight(t5),'\nExpected Answer:','False\n')