# Problem: Given an array of 0's and 1's
# Return: The number of the max consecutive 1's

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxOnes = tempOnes = 0
        for digit in nums:
        	print(digit)
        	if digit == 1:
        		tempOnes +=1
        	else:
        		if tempOnes > maxOnes:
        			maxOnes = tempOnes
        		tempOnes = 0
        if tempOnes > maxOnes:
        	maxOnes = tempOnes
        return(maxOnes)

driver = Solution()
t1 = [1,1,0,1,1,1]

print('\n')
print('Array:',t1,'\nProgram vs Expected\n',driver.findMaxConsecutiveOnes(t1),'3\n')