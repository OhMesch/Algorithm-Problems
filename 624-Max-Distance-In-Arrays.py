# Problem Statement:
# Given an array of arrays, find the maximum difference between the numbers
# Integers range from -10000 to 10000

class Solution(object):
    def maxDistance(self, arrays):
        dic = {}
        minVal = 10001
        maxVal = -10001
        for arrayIndex in range(len(arrays)):
        	if len(arrays[arrayIndex]) > 0:
        		dic[arrayIndex] = {}
        		dic[arrayIndex]['min'] = min(arrays[arrayIndex])
        		dic[arrayIndex]['max'] = max(arrays[arrayIndex])
        print(dic)
        for k,v in dic.items():
        	print('key',k,'values',v)
        	# if v['min'] < minVal:
        	# 	minVal = v['min']
        	# if v['max'] > maxVal:
        	# 	maxVal = v['max']
        	minVal = min(v['min'])
        	maxVal = max(v['max'])
        distance = abs(maxVal-minVal)
        return(distance)

driver = Solution()
t1 = [[1,2,3],[4,5],[1,2,3]]
t2 = [[1,2,3],[],[1,2,3]]
t3 = [[1,4],[0,5]]
print(driver.maxDistance(t1),'answer=4')
print(driver.maxDistance(t2),'answer=2')
print(driver.maxDistance(t3),'answer=4')

# class Solution(object):
# 	def maxDistance(self, arrays):
# 		min = 10001
# 		max = -10001
# 		for array in arrays:
# 			if len(array) == 0:
# 				break
# 			for elm in array:
# 				if elm < min:
# 					min = elm
# 				if elm > max:
# 					max = elm 
# 		range = abs(max-min)
# 		return(range)

# driver = Solution()
# t1 = [[1,2,3],[4,5],[1,2,3]]
# t2 = [[1,2,3],[],[1,2,3]]
# t3 = [[1,4],[0,5]]
# print(driver.maxDistance(t1))
# print(driver.maxDistance(t2))
# print(driver.maxDistance(t3))