'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
'''
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(-1)
        lsum = 0
        rsum = sum(nums[1:])
        i = 0
        while i < len(nums)-1:
            if lsum == rsum:
                return(i)
            rsum-=nums[i+1]
            lsum+=nums[i]
            i+=1
        if sum(nums[:-1]) == 0:
            return(len(nums)-1)
        return(-1)