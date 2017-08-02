# Problem: 
# Given a sorted array consisting of only integers where every element appears twice
# except for one element which appears once. 

# Return: 
# The the element that only appears once

# Notes:
'''
Requires O(logn) time complexity
Requires O(1) space complexity
'''
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while True:
            mid = len(nums)//2
            if len(nums) < 2:
                if len(nums) == 1:
                    return(nums[mid])
                else:
                    return(0)
            # print(nums)
            # print("Mid i: %d, Mid val: %d" % (mid,nums[mid]))
            if nums[mid] == nums[mid-1]:
                if len(nums[:mid-1])%2 != 0:
                    nums = nums[:mid-1]
                else:
                    nums = nums[mid+1:]
            elif nums[mid] == nums[mid+1]:
                if len(nums[:mid])%2 != 0:
                    nums = nums[:mid]
                else:
                    nums = nums[mid+2:]
            else:
                return(nums[mid])
driver = Solution()
t1 = [1,1,2,3,3,5,5]
t2 = [1,1,2,3,3,4,4,8,8]
t3 = [3,3,7,7,10,11,11]
t4 = [10,10,11,11,14,16,16,20,20,24,24,50,50,51,51,54,54,78,78,80,80]
t5 = [1,1,2]
t6 = [1]
t7 = []


print('\n')
#Program output vs expected output for each test case
print(driver.singleNonDuplicate(t1),'2\n')
print(driver.singleNonDuplicate(t2),'2\n')
print(driver.singleNonDuplicate(t3),'10\n')
print(driver.singleNonDuplicate(t4),'14\n')
print(driver.singleNonDuplicate(t5),'2\n')
print(driver.singleNonDuplicate(t6),'1\n')
print(driver.singleNonDuplicate(t7),'0\n')