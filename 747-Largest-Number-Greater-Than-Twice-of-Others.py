# Problem:
# In a given integer array nums, there is always exactly one largest element.

# Find whether the largest element in the array is at least twice as much as every other number in the array.

# If it is, return the index of the largest element, otherwise return -1.
 
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return(0)
        d = {}
        for index,elm in enumerate(nums):
            d[elm]=index
        sorted_nums = sorted(nums,reverse = True)
        if sorted_nums[0] >= sorted_nums[1]*2:
            return(d[sorted_nums[0]])
        else:
            return(-1)
        