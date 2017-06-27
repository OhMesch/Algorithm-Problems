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
					if 2*unique[i] > unique[j]:
						if occur[unique[i]] == 2:
							solCount += occur[unique[j]]
						else:
							solCount += ((self.factorial(occur[unique[i]]))/(2*self.factorial(occur[unique[i]]-2))*occur[unique[j]])
					else:
						break

				for k in range(i+2,len(unique)):
					if (unique[i]+unique[j] > unique[k]) and (unique[j]+unique[k] > unique[i]) and (unique[k]+unique[i] > unique[j]):
						solCount += occur[unique[i]]*occur[unique[j]]*occur[unique[k]]
						break
		return(int(solCount))

	def factorial(self, a):
		"""
		:type a: int
		:rtype: int
		"""
		if a <= 1:
			return(1)
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
t6 = [2,2,5,5,5,5,5]


print('\n')
print('\n',driver.triangleNumber(t1),"Answer = 3")
print('\n',driver.triangleNumber(t2),"Answer = 51")
print('\n',driver.triangleNumber(t3),"Answer = 5")
print('\n',driver.triangleNumber(t4),"Answer = 3")
print('\n',driver.triangleNumber(t5),"Answer = 4")
print('\n',driver.triangleNumber(t6),"Answer = 10")