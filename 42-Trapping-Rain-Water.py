# Problem: Given an array of integers representing an elevation map
# Return: The amount of water that can be collected

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        waterLevels = (self.water(height,len(height)))
        sol = waterLevels[0]

        if waterLevels[1] != 0 and waterLevels[2] < len(height) - 1:
            segment = height[waterLevels[2]:len(height)]
            segment.reverse()
            sol+=(self.water(segment,len(segment)))[0]

        return(sol)
    def water(self,array,l):
        """
        :type height: List[int]
        :rtype: array
        """
        i = 0
        water=0
        waterTemp = 0
        prevH = 0
        prevI = 0

        while i < l:
            if array[i] >= prevH:
                water += waterTemp
                waterTemp = 0
                prevH = array[i]
                prevI = i
                i+=1
                continue
            if array[i] < prevH:
                waterTemp+= prevH-array[i]
                i+=1
        return([water,waterTemp,prevI])
# -----------------------------------------------------------------------
driver = Solution()

t0 = [0,1,0,2,1,0,1,3,2,1,2,1]
t1 = [2,3,1,1,4]
t2 = [3,2,1,0,4]
t3 = [0]
t4 = [2,5,0,0]
t5 = [2,3,1,0,4,2,1,0,4,3,4,5,2,2,2,5,7,0,1,0,7,6,5,4,3,2,1,0]
t6 = [1,1,1,1]
t7 = [0,1,2,3,4,5,6,7]

print('\n')
print('Mountain Range:',t0,'Program vs Expected sol:\n',driver.trap(t0),'\n 6\n')
print('Mountain Range:',t1,'Program vs Expected sol:\n',driver.trap(t1),'\n 4\n')
print('Mountain Range:',t2,'Program vs Expected sol:\n',driver.trap(t2),'\n 6\n')
print('Mountain Range:',t3,'Program vs Expected sol:\n',driver.trap(t3),'\n 0\n')
print('Mountain Range:',t4,'Program vs Expected sol:\n',driver.trap(t4),'\n 0\n')
print('Mountain Range:',t5,'Program vs Expected sol:\n',driver.trap(t5),'\n 44\n')
print('Mountain Range:',t6,'Program vs Expected sol:\n',driver.trap(t6),'\n 0\n')
print('Mountain Range:',t7,'Program vs Expected sol:\n',driver.trap(t7),'\n 0\n')
