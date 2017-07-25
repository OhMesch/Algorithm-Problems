# Problem: Given a 2D array representing islands and ocean
# Return: The number of unique islands

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return(0)
        sol = 0
        oceanMap = [[char for char in elm] for elm in grid]
        checked = [[0 for y in oceanMap[0]] for x in oceanMap]

        for x in range(len(oceanMap[0])):
            for y in range(len(oceanMap)):
                if checked[y][x] == 1:
                    continue
                if oceanMap[y][x] == '1':
                    sol+=1
                    self.islandHelper(oceanMap,x,y,checked)
        return(sol)

    def islandHelper(self,islandArr,x,y,checkedArr):
        if islandArr[y][x] == '1' and checkedArr[y][x] == 0:
            checkedArr[y][x] = 1
            if y-1 >= 0 and checkedArr[y-1][x] == 0:
                self.islandHelper(islandArr,x,y-1,checkedArr)
            if x-1 >= 0 and checkedArr[y][x-1] == 0:
                self.islandHelper(islandArr,x-1,y,checkedArr)
            if y+1 < len(islandArr) and checkedArr[y+1][x] == 0:
                self.islandHelper(islandArr,x,y+1,checkedArr)
            if x+1 < len(islandArr[0]) and checkedArr[y][x+1] == 0:
                self.islandHelper(islandArr,x+1,y,checkedArr)
#-------------------------------------------------------------------------
driver = Solution()
t0 = ["11110","11010","11000","00000"]
t1 = ['11110','11010','11000','00000']
t2 = ['11000','11000','00100','00011']
t3 = ['00000','00000','00000','00000']
t4 = ['10000','01000','00010','00001']
t5 = ['11111','11111','11111','11111']
t6 = ['11111','00100','00100','11111']
t7 = ['1']

print('\n')
print(driver.numIslands(t0),'1')
print(driver.numIslands(t1),'1')
print(driver.numIslands(t2),'3')
print(driver.numIslands(t3),'0')
print(driver.numIslands(t4),'4')
print(driver.numIslands(t5),'1')
print(driver.numIslands(t6),'1')
print(driver.numIslands(t7),'1')