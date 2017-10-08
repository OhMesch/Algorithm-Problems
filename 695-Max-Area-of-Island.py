'''
Problem:
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.) 
'''


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return(0)
        self.sol = 0
        oceanMap = [[char for char in elm] for elm in grid]
        checked = [[0 for y in oceanMap[0]] for x in oceanMap]

        for x in range(len(oceanMap[0])):
            for y in range(len(oceanMap)):
                if checked[y][x] == 1:
                    continue
                if oceanMap[y][x] == 1:
                    self.islandHelper(oceanMap,x,y,checked)
        return(self.sol)

    def islandHelper(self,islandArr,x,y,checkedArr,area=1):
        if islandArr[y][x] == 1 and checkedArr[y][x] == 0:
            checkedArr[y][x] = 1
            if y-1 >= 0 and checkedArr[y-1][x] == 0:
                area += self.islandHelper(islandArr,x,y-1,checkedArr)
            if x-1 >= 0 and checkedArr[y][x-1] == 0:
                area+= self.islandHelper(islandArr,x-1,y,checkedArr)
            if y+1 < len(islandArr) and checkedArr[y+1][x] == 0:
                area+= self.islandHelper(islandArr,x,y+1,checkedArr)
            if x+1 < len(islandArr[0]) and checkedArr[y][x+1] == 0:
                area+= self.islandHelper(islandArr,x+1,y,checkedArr)
            if area > self.sol:
                self.sol = area
            return(area)
        
        else:
            return(0)