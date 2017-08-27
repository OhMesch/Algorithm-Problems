# Problem: Given an array of integers
# Return: Check if it could become non-decreasing by modifying at most 1 element
# Note: Define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n)

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
        	return(True)
        for i in range(len(nums)-1):
        	if nums[i] > nums[i+1]:
        		return((nums[:i]+nums[i+1:])==list(sorted(nums[:i]+nums[i+1:]))or(nums[:i+1]+nums[i+2:])==list(sorted(nums[:i+1]+nums[i+2:])))
        return(True)

driver = Solution()
print('\n')

print('1')
print('**',driver.checkPossibility([1,1,1]))
print('-- True\n')

print('2')
print('**',driver.checkPossibility([2,3,3,2,4]))
print('-- True\n')

print('3')
print('**',driver.checkPossibility([4,2,3]))
print('-- True\n')

print('4')
print('**',driver.checkPossibility([2,4,5,3]))
print('-- True\n')

print('5')
print('**',driver.checkPossibility([3,4,2,2]))
print('-- False\n')