# Problem Statement: Given an array of non-negative integers representing side-length
# Return the number of triplets that can form triangles

# Status: In progress 40%

class Solution(object):
	def triangleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		occur = {}
		unique = []
		solCount = 0

		nums.sort()

		for number in nums:
			if number not in occur:
				occur[number] = 1
				unique.append(number)
			else:
				occur[number] += 1

		for i in range(len(unique)):

			if occur[unique[i]] >= 3: 
				#equalilateral
				if occur[unique[i]] == 3:
					solCount += 1
				else:
					solCount += (self.factorial(occur[unique[i]]))/(6*self.factorial(occur[unique[i]]-3))

			for j in range(i+1,len(unique)):

				if occur[unique[i]] >= 2:
					#iso
					#check i and j
					#if i and j are tri
						solCount += 1
						#relation between number and sol
					#I and j not tri
						#j is too big
						break

				for k in range(i+2,len(unique)):
					#i j k are tri
						solCount += 1
						#relation between number and sol
					#are not tri:
						break
		return(int(solCount))

	def factorial(self, a):
		"""
		:type a: int
		:rtype: int
		"""

		fact = 1
		while a > 1:
			fact = fact * a
			a -= 1
		return(int(fact))

driver = Solution()

t1 = [2,2,3,4]
t2 = [14,45,70,34,17,17,45,45,45]
t3 = [82,10,63,49,72]
t4 = [5,22,62,39,64]
t5 = [1,40,98,77,85]
t6 = [5,5,5,5,5]

print('\n')
print('\n',driver.triangleNumber(t1),"Answer = 3")
print('\n',driver.triangleNumber(t2),"Answer = 51")
print('\n',driver.triangleNumber(t3),"Answer = 5")
print('\n',driver.triangleNumber(t4),"Answer = 3")
print('\n',driver.triangleNumber(t5),"Answer = 4")
print('\n',driver.triangleNumber(t6),"Answer = 10")