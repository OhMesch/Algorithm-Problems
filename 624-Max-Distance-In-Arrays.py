# Problem Statement:
# Given an array of arrays, find the maximum difference between the numbers
# Integers range from -10000 to 10000

# Current issues: Will select values from the same array if it is one of first two non-empty arrays

class Solution(object):
	def maxDistance(self, arrays):
		maxArr = []
		minArr = []
		for indvArr in arrays:
			if len(indvArr) == 0:
				continue
			maxArr.append(max(indvArr))
			minArr.append(min(indvArr))

		print(arrays,'\nMax=',maxArr,'\nMin=',minArr) #---------------------------

		absMax = max(maxArr)
		absMin = min(minArr)

		for index in range(len(minArr)):
			
			
driver = Solution()
t1 = [[1,2,3],[4,5],[1,2,3]]
t2 = [[1,2,3],[],[1,2,3]]
t3 = [[1,4],[0,5]]
t4 = [[1,2,3],[8],[1,2,3]]
t5 = [[7,0],[6,2]]
t6 = [[7,7],[7,7]]
t7 = [[7,0],[6,2],[7,0]]

print('\n')
print('\n',driver.maxDistance(t1),'answer=4\n')
print('\n',driver.maxDistance(t2),'answer=2\n')
print('\n',driver.maxDistance(t3),'answer=4\n')
print('\n',driver.maxDistance(t4),'answer=7\n')
print('\n',driver.maxDistance(t5),'answer=6\n')
print('\n',driver.maxDistance(t6),'answer=0\n')
print('\n',driver.maxDistance(t7),'answer=7\n')


