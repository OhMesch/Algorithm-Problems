# # Problem Statement:
# # Given an array of integers 
# # Find all unique triplets in the array which gives the sum of zero.

class Solution:
	def threeSum(self, nums):
		
		if len(nums) < 3:
			return([])

		dictionary = {}
		output = []
		for i in range(len(nums)):
			target = -nums[i]
			if nums[i] in dictionary:
				dictionary[nums[i]]['count'] +=1
			# 2 Sum
			for j in range(len(nums)):
				if (target - nums[j]) in dictionary:
					if self.isUniqueTrue(nums[i],target - nums[j],nums[j],output,nums,dictionary):
						output.append([nums[i],target - nums[j],nums[j]])
				else:
					if nums[j] not in dictionary:
						dictionary[nums[j]] = {}
						if j == 0:
							dictionary[nums[j]]['count'] = 1
						else:
							dictionary[nums[j]]['count'] = 0
					dictionary[nums[j]]['position'] = j
		return(output)

	def isUniqueTrue(self,a1,a2,a3,sol,nums,dictionary):
		print(dictionary)
		if a1 + a2 + a3 != 0:
			return(False)
		if (a1 == a2 or a1 == a3) and dictionary[a1]['count'] < 2:
			return(False)
		if a2 == a3 and dictionary[a2]['count'] < 2:
			return(False)
		if (a1 == a2 == a3 and a1 != 0):
			return(False)
		if a1 == a2 == a3 and dictionary[0]['count'] < 3:
			return(False)
		for array in sol:
			if a1 in array and a2 in array and a3 in array:
				if a1 == a2 == a3 == 0 and [0,0,0] not in sol and dictionary[0]['count'] > 2:
					return(True)
				else:
					return(False)
		return(True)

driver = Solution()
t1 = [-1,0,1,2,-1,-4]
t2 = [1,2,-2,-1]
t3 = [0,0]
t4 = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
t5 = [0,0,0]
t6 = [-1,0,1,2,-1,-4]
t7 = [3,0,-2,-1,1,2]
print(driver.threeSum(t1))
print(driver.threeSum(t2))
print(driver.threeSum(t3))
print(driver.threeSum(t4))
print(driver.threeSum(t5))
print(driver.threeSum(t6))
print(driver.threeSum(t7))

