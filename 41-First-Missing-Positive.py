# Problem: Given an unsorted integer array
# Return: First missing positive integer

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       	sortedNums = sorted(list(filter(lambda x: x > 0,nums)))
       	#Case-All numbers neg: First postive number is 1
       	if len(sortedNums) == 0:
       		return(1)
       	#Case-1 is missing- First postive number is 1
       	elif sortedNums[0] != 1:
       		return(1)
       	#Case-skip in numbers- Postive number is one skipped
        for i in range(1,len(sortedNums)):
        	if sortedNums[i] == sortedNums[i-1]:
        		continue
        	elif sortedNums[i] != sortedNums[i-1]+1:
        		return(sortedNums[i-1]+1)
        #Case-No skips- Positive number is next number in sequence
        return(sortedNums[-1]+1)



driver = Solution()
t1 = [1,2,0]
t2 = [3,4,-1,1]
t3 = [-1,-2,-3]
t4 = [-1,-2,-3,3]
t5 = [0,1,1,2,2]

print('\n')
print('Array:',t1,'Program sol vs Expected sol:\n',driver.firstMissingPositive(t1),'\n 3\n')
print('Array:',t2,'Program sol vs Expected sol:\n',driver.firstMissingPositive(t2),'\n 2\n')
print('Array:',t3,'Program sol vs Expected sol:\n',driver.firstMissingPositive(t3),'\n 1\n')
print('Array:',t4,'Program sol vs Expected sol:\n',driver.firstMissingPositive(t4),'\n 1\n')
print('Array:',t5,'Program sol vs Expected sol:\n',driver.firstMissingPositive(t5),'\n 3\n')
