# Problem: Given an array of duplicates and a single number
# Return: The single number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = dict()
        for elm in nums:
            if elm in counter:
                counter[elm] += 1
            else:
                counter[elm] = 1
        return([k for k,v in counter.items() if v == 1][0])
# -----------------------------------------------------------------------
driver = Solution()

t0 = [0,0,1,1,2,2,3,3,5]
t1 = [2,3,1,1,4,3,2]

print('\n')
print('Array:',t0,'Program vs Expected sol:\n',driver.singleNumber(t0),'\n 5\n')
print('Array:',t1,'Program vs Expected sol:\n',driver.singleNumber(t1),'\n 4\n')
