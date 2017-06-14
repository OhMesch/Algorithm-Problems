# # Problem Statement:
# # Given an array of integers 
# # Find all unique triplets in the array which gives the sum of zero.

class Solution:
	def threeSum(self, nums):
		
		dictionary = {}
		output = []
		for i in range(len(nums)):
			target = -nums[i]
			# 2 Sum
			for j in range(len(nums)):
				if (target - nums[j]) in dictionary and self.isUnique(nums[i],target - nums[j],nums[j],output,nums):
						print('Output',self.isUnique(nums[i],target - nums[j],nums[j],output,nums))
						print(nums[i],target - nums[j],nums[j],output,nums)
						output.append([nums[i],target - nums[j],nums[j]])
				else:
					dictionary[nums[j]] = j
		return(output)

	def isUnique(self,a1,a2,a3,sol,nums):
		for array in sol:
			if a1 in array and a2 in array and a3 in array:
				return(False)
			if a1 + a2 + a3 != 0:
				return(False)
			if a1 == a2 and nums.count(a1) < 2:
				print("FASLE")
				return(False)
			if a2 == a3 and nums.count(a2) < 2:
				return(False)
			if a1 == a3 and nums.count(a1) < 2:
				return(False)
			if a1 == a2 == a3 and a1 != 0:
				return(False)
		print(nums,a1,a2,a3,nums.count(a1))
		return(True)


driver = Solution()
t1 = [-1,0,1,2,-1,-4]
t2 = [1,2,-2,-1]
# print(driver.threeSum(t1))
print(driver.threeSum(t2))
