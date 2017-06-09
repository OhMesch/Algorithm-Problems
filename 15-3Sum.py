# Problem Statement:
# Given an array of integers 
# Find all unique triplets in the array which gives the sum of zero.

class Solution:
	def threeSum(self, nums,target):
		
		dictionary = {}
		output = []

		for index in range(len(nums)):
			if (target - nums[index]) in dictionary:
				output.append([target - nums[index],nums[index]])
			else:
				dictionary[nums[index]] = index
		return(output)

driver = Solution()
t1 = [-1,0,1,2,-1,-4]
print(driver.threeSum(t1,-2))