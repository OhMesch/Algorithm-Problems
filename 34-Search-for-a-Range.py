'''
Problem:
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1]
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Find left bound if present
        l,r = 0,len(nums)
        seen = False
        while l<r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid
            elif nums[mid] == target:
                r = mid
                seen = True
            else:
                l = mid+1
        if not seen:
            return([-1,-1])
        
        #Find right bound
        r = l
        h = len(nums)
        while r<h:
            mid = (r+h)//2
            if nums[mid] > target:
                h = mid
            else:
                r = mid+1
        return([l,r-1])