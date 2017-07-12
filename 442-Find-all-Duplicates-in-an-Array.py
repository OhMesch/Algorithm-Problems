# Problem: Given an array of integers that either appear once or twice
# Return: All integers that appear twice

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        solution = []
        for number in nums:
        	if number in d:
        		d[number]+=1
        		solution.append(number)
        	else:
        		d[number] = 1
        return(sorted(solution))

driver = Solution()

t1 = [4,3,2,7,8,2,3,1]

print('\n')
print('Array:',t1,'\nProgram Sol vs Expected Sol\n', driver.findDuplicates(t1),'\n[2,3]')`