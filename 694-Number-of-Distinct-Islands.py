'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
'''

class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        unique = {}
        if grid == []:
            return(0)
        sol = 0
        oceanMap = [[char for char in elm] for elm in grid]
        checked = [[0 for y in oceanMap[0]] for x in oceanMap]

        for x in range(len(oceanMap[0])):
            for y in range(len(oceanMap)):
                if checked[y][x] == 1:
                    continue
                if oceanMap[y][x] == 1:
                    island=(self.islandHelper(oceanMap,x,y,checked))
                    if island not in unique:
                        unique[island] = 1
                        sol+=1
        return(sol)

    def islandHelper(self,islandArr,x,y,checkedArr,garbage=1):
        if islandArr[y][x] == 1 and checkedArr[y][x] == 0:
            checkedArr[y][x] = 1
            if y-1 >= 0 and checkedArr[y-1][x] == 0:
                if islandArr[y-1][x] == 1:
                    garbage+=3+(2*self.islandHelper(islandArr,x,y-1,checkedArr,garbage))
                else:
                    self.islandHelper(islandArr,x,y-1,checkedArr,garbage)
            if x-1 >= 0 and checkedArr[y][x-1] == 0:
                if islandArr[y][x-1] == 1:
                    garbage+=12-(4*self.islandHelper(islandArr,x-1,y,checkedArr,garbage))
                else:
                    self.islandHelper(islandArr,x-1,y,checkedArr,garbage)
            if y+1 < len(islandArr) and checkedArr[y+1][x] == 0:
                if islandArr[y+1][x] == 1:
                    garbage+=16*(3+self.islandHelper(islandArr,x,y+1,checkedArr,garbage))
                else:
                    self.islandHelper(islandArr,x,y+1,checkedArr,garbage)
            if x+1 < len(islandArr[0]) and checkedArr[y][x+1] == 0:
                if islandArr[y][x+1] == 1:
                    garbage+=18*self.islandHelper(islandArr,x+1,y,checkedArr,garbage)
                else:
                    self.islandHelper(islandArr,x+1,y,checkedArr,garbage)
            return(garbage)
        return(4)
        