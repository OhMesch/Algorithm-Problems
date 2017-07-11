# Problem: Given two integers
# Return: Return the hamming distance between the two

class Solution(object):
	def hammingDistance(self, x, y):
		"""
		:type x: int
		:type y: int
		:rtype: int
		"""
		b1,b2 = list(format(x,'32b')),list(format(y,'32b'))
		hammingDist = 0
		b1,b2 = ['0' if x == " " else x for x in b1] , ['0' if x == " " else x for x in b2]
		for i in range(len(b1)):
			if b1[i] != b2[i]:
				hammingDist+= 1
		return(hammingDist)

driver = Solution()

x1 = 1
y1 = 4
x2 = 167
y2 = 3456

print('\n')
print('Numbers:',x1,y1, '\nHamming Distance:',driver.hammingDistance(x1,y1),'\nExpected Answer:','2\n')
print('Numbers:',x2,y2, '\nHamming Distance:',driver.hammingDistance(x2,y2),'\nExpected Answer:','7\n')