# Problem: Given an array from 1 to n with a missing number and a duplicate number
# Return: The duplicate and missing numbers

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        a = set(range(1,max(nums)+1))
        missing = (set(nums)^a)
        for i in range(1,len(nums)):
            if nums[i] == nums [i-1]:
                double = nums[i]
                if missing:
                    return([double,list(missing)[0]])
        if nums[-1] == nums[-2] and nums[-1] == double:
            return([double,double+1])
        if nums[0] == nums[1] and nums[0] == double:
            return([double,double-1])
        if not missing:
            missing = [max(nums)+1]

        return([double,list(missing)[0]])



driver = Solution()
t1 = [1,2,2,4]
t2 = [3,2,3,4,6,5]
t3 = [1,5,3,2,2,7,6,4,8,9]
t4 = [2,2]

print('\n')
print(driver.findErrorNums(t1),'[2,3]')
print(driver.findErrorNums(t2),'[3,1]')
print(driver.findErrorNums(t3),'[2,10]')
print(driver.findErrorNums(t4),'[2,1]')