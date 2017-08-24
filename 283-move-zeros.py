# Problem: Given an array of integers
# Return: The array with all zeros at the end
# Notet: Must be in-place

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        w=0
        r=0
        zeros=0
        while r < len(nums) and w < len(nums)-zeros:
            while r < len(nums) and nums[r] == 0:
                r+=1
                zeros+=1
            while r < len(nums) and nums[r]:
                nums[w], nums[r] = nums[r], nums[w]
                w+=1
                r+=1

        return(nums)

driver = Solution()

print('\n')

print('1')
print('**',driver.moveZeroes([0,1,3,0,12,0]))
print('-- [1, 3, 12, 0, 0, 0]')

print('2')
print('**',driver.moveZeroes([]))
print('-- []')

print('3')
print('**',driver.moveZeroes([0,0,0,0,0,0]))
print('-- [0, 0, 0, 0, 0, 0]')

print('4')
print('**',driver.moveZeroes([1,2,3,4,5,6]))
print('-- [1, 2, 3, 4, 5, 6]')

print('5')
print('**',driver.moveZeroes([0,0,0,4,5,6]))
print('-- [4, 5, 6, 0, 0, 0]')