'''
Problem:
Given an unsorted array of integers, find the length of longest continuous increasing subsequence. 
'''

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return(0)
        elif len(nums) == 1:
            return(1)
        max_len = 0
        curr = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr+=1
            else:
                curr = 1
            max_len = max(curr,max_len)
        return(max_len)