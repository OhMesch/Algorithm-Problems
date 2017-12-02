# Problem:
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array. 

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for elm,expected in zip(sorted(nums),list(range(max(nums)+1))):
            if elm != expected:
                return(expected)
        return(elm+1)