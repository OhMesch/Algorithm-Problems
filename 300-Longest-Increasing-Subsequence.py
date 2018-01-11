# Problem:

# Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

# Your algorithm should run in O(n2) complexity. 

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)

        history = len(nums)*[1]

        for i in range(len(nums)-2,-1,-1):
            orig = nums[i]
            temp = 0
            # print("original:",nums[i])
            for j in range(i+1,len(nums)):
                # print("compare:",nums[j])
                compar = nums[j]
                if compar > orig and history[j] > temp:
                    # print(history)
                    temp = history[j]
            history[i]+=temp

        return(max(history))

        # CONSIDER IMPROVING WITH LSIT COMPREHENSION
        
driver = Solution()

print('1')
print("**",driver.lengthOfLIS([1,1]))
print("-- 1\n")

print('2')
print("**",driver.lengthOfLIS([4,7]))
print("-- 2\n")

print('3')
print("**",driver.lengthOfLIS([19,7,19,20,4,5,13,10]))
print("-- 3\n")

print('4')
print("**",driver.lengthOfLIS([5,5,2,7,3,9]))
print("-- 3\n")

print('5')
print("**",driver.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print("-- 4\n")