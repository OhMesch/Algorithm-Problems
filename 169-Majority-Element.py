# Problem Statement: Given a non-empty array of integers
# Return: The majority element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = []
        for elm in nums:
            if elm not in unique:
                if nums.count(elm) >= len(nums)/2.0:
                    return(elm)
                else:
                    unique.append(elm)


driver = Solution()

t1 = [1,1,2,3]
t2 = [6,5,5]

print('\n')
print(driver.majorityElement(t1),'Answer:1\n')
print(driver.majorityElement(t2),'Answer:5\n')
