# Problem Statement:
# Given an array of arrays, find the maximum difference between the numbers
# Integers range from -10000 to 10000

# Final Solution

class Solution(object):
	def maxDistance(self, arrays):

		maxArr = []
		minArr = []
		maxDis = 0
		occurences = {}

		for indvArr in arrays:
			if len(indvArr) != 0:
				maxArr.append(indvArr[-1])
				minArr.append(indvArr[0])

		for i in range(len(maxArr)):
			lowest = 10001

			if maxArr[i] in occurences:
				occurences[maxArr[i]] += 1
			else:
				occurences[maxArr[i]] = 1

			if occurences[maxArr[i]] < 3:
				for j in range(i):
					if minArr[j] < lowest:
						lowest = minArr[j]
						currDis = abs(maxArr[i]-minArr[j])
						if currDis > maxDis:
							maxDis = currDis

				for k in range(i+1,len(minArr)):
					if minArr[k] < lowest:
						lowest = minArr[k]
						currDis = abs(maxArr[i]-minArr[k])
						if currDis > maxDis:
							maxDis = currDis

		return(maxDis)

driver = Solution()
t1 = [[1,2,3],[4,5],[1,2,3]]
t2 = [[1,2,3],[],[1,2,3]]
t3 = [[1,4],[0,5]]
t4 = [[1,2,3],[8],[1,2,3]]
t5 = [[0,7],[2,6]]
t6 = [[7,7],[7,7]]
t7 = [[0,7],[2,6],[0,7]]
t8 = [[0,7],[-1,6],[-2,5]]
t9 = [[-2,7],[-1,6]]
t10 = [[1,2,3,15],[4,5,15],[1,2,3,15],[6,7,8,15]]


print('\n')
print('\n',driver.maxDistance(t1),'answer = 4\n')
print('\n',driver.maxDistance(t2),'answer = 2\n')
print('\n',driver.maxDistance(t3),'answer = 4\n')
print('\n',driver.maxDistance(t4),'answer = 7\n')
print('\n',driver.maxDistance(t5),'answer = 6\n')
print('\n',driver.maxDistance(t6),'answer = 0\n')
print('\n',driver.maxDistance(t7),'answer = 7\n')
print('\n',driver.maxDistance(t8),'answer = 9\n')
print('\n',driver.maxDistance(t9),'answer = 8\n')
print('\n',driver.maxDistance(t10),'answer = 15\n')
