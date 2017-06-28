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
		solutions = []

		nums.sort()

		if len(nums) <3:
			return(0)

		for number in nums:
			if number != 0:
				if number not in occur:
					occur[number] = 1
					unique.append(number)
				else:
					occur[number] += 1

		for i in range(len(unique)):

			if occur[unique[i]] >= 3: 
				#equalilateral
				if occur[unique[i]] == 3:
					# solutions.append([unique[i],unique[i],unique[i]])
					solCount += 1
				else:
					# solutions.append([unique[i],unique[i],unique[i]])
					solCount += (self.factorial(occur[unique[i]]))/(6*self.factorial(occur[unique[i]]-3))

			for j in range(i+1,len(unique)):

				if occur[unique[i]] >= 2:
					#iso
					if 2*unique[i] > unique[j]:
						if occur[unique[i]] == 2:
							# solutions.append([unique[i],unique[i],unique[j]])
							solCount += occur[unique[j]]
						else:
							# solutions.append([unique[i],unique[i],unique[j]])
							solCount += ((self.factorial(occur[unique[i]]))/(2*self.factorial(occur[unique[i]]-2))*occur[unique[j]])

				if occur[unique[j]] == 2:
					# solutions.append([unique[i],unique[j],unique[j]])
					solCount +=occur[unique[i]]
				elif occur[unique[j]] > 2:
					# solutions.append(['test',unique[i],unique[j],unique[j]])
					solCount += ((self.factorial(occur[unique[j]]))/(2*self.factorial(occur[unique[j]]-2))*occur[unique[i]])

				for k in range(j+1,len(unique)):
					if (unique[i]+unique[j] > unique[k]) and (unique[j]+unique[k] > unique[i]) and (unique[k]+unique[i] > unique[j]):
						# solutions.append([unique[i],unique[j],unique[k]])
						solCount += occur[unique[i]]*occur[unique[j]]*occur[unique[k]]
					else:
						break
		# print(solutions)
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
t7 = [2,2,5,5,5,5,5,0,0]
t8 = [0,0,0]


print('\n')
print('t1',driver.triangleNumber(t1),"Answer = 3\n")
print('t2',driver.triangleNumber(t2),"Answer = 51\n")
print('t3',driver.triangleNumber(t3),"Answer = 5\n")
print('t4',driver.triangleNumber(t4),"Answer = 3\n")
print('t5',driver.triangleNumber(t5),"Answer = 4\n")
print('t6',driver.triangleNumber(t6),"Answer = 30\n")
print('t7',driver.triangleNumber(t7),"Answer = 30\n")
print('t8',driver.triangleNumber(t8),"Answer = 0\n")