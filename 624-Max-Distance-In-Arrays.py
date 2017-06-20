# Problem Statement:
# Given an array of arrays, find the maximum difference between the numbers
# Integers range from -10000 to 10000

class Solution(object):
    def maxDistance(self, arrays):
        
        minVal = 10001
        maxVal = -10001
        for arr in arrays:
            print('current array is',arr)
            if len(arr) == 0:
                break
            if min(arr) < minVal and max(arr) > maxVal:
                print("min and max",minVal,maxVal)
                diffMin = abs(min(arr)-minVal)
                diffMax = abs(max(arr)-maxVal)
                print('diffs are',diffMin,diffMax)
                if diffMin <= diffMax:
                    print('replace Max',max(arr))
                    maxVal = max(arr) #Would setting a temp var to max and min be faster than calling function?
                else:
                    print('replace Min',min(arr))
                    minVal = min(arr)
            elif min(arr) < minVal:
                minVal = min(arr)
            elif max(arr) > maxVal:
                maxVal = max(arr)
            print('min and max values',minVal,maxVal)

driver = Solution()
t1 = [[1,2,3],[4,5],[1,2,3]]
t2 = [[1,2,3],[],[1,2,3]]
t3 = [[1,4],[0,5]]
t4 = [[1,2,3],[8],[1,2,3]]
print(driver.maxDistance(t1),'answer=4')
print(driver.maxDistance(t2),'answer=2')
print(driver.maxDistance(t3),'answer=4')
print(driver.maxDistance(t4),'answer=7')

# class Solution(object):
#     def maxDistance(self, arrays):
#         dic = {}
#         minVal = 10001
#         maxVal = -10001
#         for arrayIndex in range(len(arrays)):
#         	if len(arrays[arrayIndex]) > 0:
#         		dic[arrayIndex] = {}
#         		dic[arrayIndex]['min'] = min(arrays[arrayIndex])
#         		dic[arrayIndex]['max'] = max(arrays[arrayIndex])
#         print(dic)
#         for k,v in dic.items():
#         	print('key',k,'values',v)
#         	# if v['min'] < minVal:
#         	# 	minVal = v['min']
#         	# if v['max'] > maxVal:
#         	# 	maxVal = v['max']
#         	minVal = min(v['min'])
#         	maxVal = max(v['max'])
#         distance = abs(maxVal-minVal)
#         return(distance)

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