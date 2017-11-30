# Problem:
# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet. 

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        survivors = []
        pos = []
        for elm in asteroids:
        	if elm > 0:
        		pos.append(elm)
        	else:
        		neg = True
        		while pos and neg:
        			pos_top = pos.pop()
        			if pos_top > abs(elm):
        				pos.append(pos_top)
        				neg = False
        			elif pos_top == abs(elm):
        				neg = False
        	if not pos and neg:
       			survivors.append(elm)
        return(survivors+pos)

driver = Solution()
print("\n")

print('1')
print('**',driver.asteroidCollision([5, 10, -5]))
print('-- [5, 10]\n')

print('2')
print('**',driver.asteroidCollision([8, -8]))
print('-- []\n')

print('3')
print('**',driver.asteroidCollision([10, 2, -5]))
print('-- [10]\n')

print('4')
print('**',driver.asteroidCollision([-2, -1, 1, 2]))
print('-- [-2, -1, 1, 2]\n')

print('5')
print('**',driver.asteroidCollision([10,-2,-4,-5]))
print('-- [10]\n')

print('6')
print('**',driver.asteroidCollision([10, 5, -6, 7, -6]))
print('-- [10, 7]\n')

print('7')
print('**',driver.asteroidCollision([-3, -5, 10, 5, -6, 7, -6]))
print('-- [-3, -5, 10, 7]\n')