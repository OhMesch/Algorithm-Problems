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
print('Number',t1, '\n1 Bits:',driver.hammingWeight(t1),'\nExpected Answer:','2\n')
print('Number',t2, '\n1 Bits:',driver.hammingWeight(t2),'\nExpected Answer:','3\n')
print('Number',t3, '\n1 Bits:',driver.hammingWeight(t3),'\nExpected Answer:','1\n')
print('Number',t4, '\n1 Bits:',driver.hammingWeight(t4),'\nExpected Answer:','1\n')
print('Number',t5, '\n1 Bits:',driver.hammingWeight(t5),'\nExpected Answer:','1\n')