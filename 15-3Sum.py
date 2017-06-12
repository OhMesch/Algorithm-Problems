# # Problem Statement:
# # Given an array of integers 
# # Find all unique triplets in the array which gives the sum of zero.

# class Solution:
# 	def threeSum(self, nums):
		
# 		dictionary = {}
# 		output = [[70]]
# 		for i in range(len(nums)):
# 			target = nums[i]
# 			numsReduced = nums[0:i]
# 			for k in range(i+1,len(nums)):
# 				numsReduced.append(nums[k])
# 			# 2 Sum
# 			for j in range(len(numsReduced)):
# 				if (target - nums[j]) in dictionary:
# 					l = 0
# 					while l < len(output):
# 						print('werein')
# 						if target not in output[l] or (target - nums[j]) not in output[l] or nums[j] not in output[l]:
# 							output.append([target,target - nums[j],nums[j]])
# 						l += 1
# 				else:
# 					dictionary[nums[j]] = j
# 		return(output)


# driver = Solution()
# t1 = [-1,0,1,2,-1,-4]
# # print(t1[])
# print(driver.threeSum(t1))

# Problem Statement:
# Given an array of integers 
# Find all unique triplets in the array which gives the sum of zero.

# This part shows all combination of answers

# class Solution:
# 	def threeSum(self, nums):
		
# 		dictionary = {}
# 		output = []
# 		for i in range(len(nums)):
# 			target = nums[i]
# 			numsReduced = nums[0:i]
# 			for k in range(i+1,len(nums)):
# 				numsReduced.append(nums[k])
# 			# 2 Sum
# 			for j in range(len(numsReduced)):
# 				if (target - nums[j]) in dictionary:
# 					output.append([target,target - nums[j],nums[j]])
# 				else:
# 					dictionary[nums[j]] = j
# 		return(output)

# driver = Solution()
# t1 = [-1,0,1,2,-1,-4]
# # print(t1[])
# print(driver.threeSum(t1))

class Solution:
	def threeSum(self, nums):
		
		dictionary = {}
		output = []
		for i in range(len(nums)):
			target = -nums[i]
			numsReduced = nums[0:i]
			for k in range(i+1,len(nums)):
				numsReduced.append(nums[k])
			# 2 Sum
			for j in range(len(numsReduced)):
				if (target - nums[j]) in dictionary and self.isUnique(nums[i],target - nums[j],nums[j],output):
					output.append([nums[i],target - nums[j],nums[j]])
				else:
					dictionary[nums[j]] = j
		return(output)

	def isUnique(self,a1,a2,a3,sol):
		for array in sol:
			if a1 in array and a2 in array and a3 in array:
				return(False)
		return(True)


driver = Solution()
t1 = [-1,0,1,2,-1,-4]
print(driver.threeSum(t1))
