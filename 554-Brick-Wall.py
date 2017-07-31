# Problem: 
'''
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. 
The bricks have the same height but different width. 
You want to draw a vertical line from the top to the bottom and cross the least bricks.
'''

# Return: 
# Find out how to draw the line to cross the least bricks and return the number of crossed bricks.

class Solution(object):
    def leastBricks(self, wall):
        '''
        :type wall: List[List[int]]
        :rtype: int
        '''
        height,length = len(wall),sum(wall[0])
        ends = {}

        for wallSeg in wall:
        	place = 0
        	for brick in wallSeg:
        		if place + brick == length:
        			break
        		place+=brick
        		if place in ends:
        			ends[place] += 1
        		else:
        			ends[place] = 1

        if not ends:
        	return(height)
        else:
        	return(height-(max(ends.values())))

driver = Solution()
t1 = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
t2 = [[1],[1],[1]]
t3 = [[3],[3],[3]]
t4 = [[1,2,3,4,5,6]]
t5 = [[100000000],[100000000],[100000000]]
t6 = [[6], [6], [2, 4], [6], [1, 2, 2, 1], [6], [2, 1, 2, 1], [1, 5], [4, 1, 1], [1, 4, 1], [4, 2], [3, 3], [2, 2, 2], [5, 1], [5, 1], [6], [4, 2], [1, 5], [2, 3, 1], [4, 2], [1, 1, 4], [1, 3, 1, 1], [2, 3, 1], [3, 3], [3, 1, 1, 1], [3, 2, 1], [6], [3, 2, 1], [1, 5], [1, 4, 1]]
t7 = [[100000000]]

print('\n')
#Program output vs expected output for each test case
print(driver.leastBricks(t1),'2\n')
print(driver.leastBricks(t2),'3\n')
print(driver.leastBricks(t3),'3\n')
print(driver.leastBricks(t4),'0\n')
print(driver.leastBricks(t5),'3\n')
print(driver.leastBricks(t6),'17\n')
print(driver.leastBricks(t7),'1\n')