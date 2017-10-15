'''
Problem:
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        d_first = {}
        d_last = {}
        degree = 0
        min_path = float('inf')
        for i in range(len(nums)):
        	if nums[i] not in d:
        		d[nums[i]] = 1
        		d_first[nums[i]] = i
        	else:
        		d[nums[i]]+=1
        		d_last[nums[i]] = i
        	if d[nums[i]] >= degree:
        		degree = d[nums[i]]

        if degree == 1:
        	return(1)

        for k,v in d.items():
        	if v == degree:
        		path = d_last[k]-d_first[k]
        		if path <= min_path:
        			min_path = path

        return(min_path+1)


driver = Solution()
print('\n')

print('0')
print('**',driver.findShortestSubArray([1,2,2,3,1,4,2]))
print('-- 6')

print('0')
print('**',driver.findShortestSubArray([1,1,1]))
print('-- 3')