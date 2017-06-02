class Solution:
	def twoSum(self, nums, target):
		indexOfComponets = []
		flag = 0
		for index1 in range(len(nums)):
			if flag == 1:
				break
			for index2 in range(len(nums)):
				if (nums[index1] + nums[index2] == target) and (index1 != index2):
					indexOfComponets.append(index1)
					indexOfComponets.append(index2)
					flag = 1
		finalSolution = indexOfComponets[0:2]
		return(finalSolution)

# sol = Solution()
# array = [2,7,11,15]
# number = 9
# print(sol.twoSum(array,number))
