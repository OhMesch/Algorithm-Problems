# Problem Statement: Given an array of non-negative integers representing side-length
# Return the number of triplets that can form triangles

class Solution(object):
	def triangleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		occur = {}
		unique = []

		nums.sort()

		for number in nums:
			if number not in occur:
				occur[number] = 1
				unique.append(number)
			else:
				occur[number] += 1
		print(unique,occur)

	def isTriangle(self, a,b,c):
		"""
		:type a,b,c: 
		:rtype: bool
		"""

		if (a + b < c) or (b + c < a) or (c + a < b):
			return(False)
		return(True)
		
driver = Solution()

t1 = [2,2,3,4]
t2 = [14,45,70,34,17,17,45,45,45]
t3 = [82,10,63,49,72]
t4 = [5,22,62,39,64]
t5 = [1,40,98,77,85]

print('\n')
print('\n',driver.triangleNumber(t1),"Answer = 3")
print('\n',driver.triangleNumber(t2),"Answer = ")
print('\n',driver.triangleNumber(t3),"Answer = ")
print('\n',driver.triangleNumber(t4),"Answer = ")
print('\n',driver.triangleNumber(t5),"Answer = ")