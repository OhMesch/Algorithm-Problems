'''
Problem:
 There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1. 
'''

class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        pos = len(flowers)*[0]
        for day,position in enumerate(flowers):
            pos[position-1] = 1

            if k < position-1:
            	no_ones = True
            	spaces = k
            	curr = position-2
            	while spaces > 0:
            		if pos[curr] == 1:
            			no_ones = False
            			break
            		curr -= 1
            		spaces -= 1
            	if no_ones and pos[curr] == 1:
            		return(day+1)

            if position+k < len(flowers):
            	no_ones = True
            	spaces = k
            	curr = position
            	while spaces > 0:
            		if pos[curr] == 1:
            			no_ones = False
            			break
            		curr += 1
            		spaces -= 1
            	if no_ones and pos[curr] == 1:
            		return(day+1)

        return(-1)
        	

driver = Solution()
print('\n')

print('1')
print('**',driver.kEmptySlots([1,3,2],1))
print('-- 2\n')

print('2')
print('**',driver.kEmptySlots([3,1,2],1))
print('-- 2\n')

print('3')
print('**',driver.kEmptySlots([1,2,3],1))
print('-- -1\n')

print('4')
print('**',driver.kEmptySlots([1,3,4,5,2],3))
print('-- -1\n')

print('5')
print('**',driver.kEmptySlots([1,3,4,2],2))
print('-- -1\n')

print('6')
print('**',driver.kEmptySlots([1,5,2,3,4],3))
print('-- 2\n')

print('7')
print('**',driver.kEmptySlots([1,6,7,8,5,2,3,4],3))
print('-- 5\n')

print('8')
print('**',driver.kEmptySlots([1,6,7,8,5,2,3,4],0))
print('-- 3\n')
#nlogn if you treat like insertion sort using binary search, get higher and lower that way and take difference