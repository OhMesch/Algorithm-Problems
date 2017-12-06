# Problem:
# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value. 

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_val = sum(nums[:k])
        max_val = curr_val
        for i in range(k,len(nums)):
            curr_val = curr_val - nums[i-k] + nums[i]
            if curr_val > max_val:
                max_val = curr_val
        return(float(max_val)/k)