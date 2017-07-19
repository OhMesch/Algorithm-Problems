# Problem: Given an array of integers
# Return: Whether the array is non-unique

class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) != len(nums):
            return(True)
        else:
            return(False)

t1 = []
t2 = [1,2,3]
t3 = [1,2,3,3]

driver = Solution()

print('\n')
print('Array:',t1,'Program vs Expected:\n',driver.containsDuplicate(t1),'\n False')
print('Array:',t2,'Program vs Expected:\n',driver.containsDuplicate(t2),'\n False')
print('Array:',t3,'Program vs Expected:\n',driver.containsDuplicate(t3),'\n True')
