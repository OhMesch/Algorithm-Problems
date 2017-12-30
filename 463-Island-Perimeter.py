# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.perm = 0
        self.checked = [[0 for i in grid[0]] for j in grid]
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    self.checked[y][x] = 1
                    self.recurseIsland(grid,x,y)
                    return(self.perm)
                
    def recurseIsland(self,grid,x,y):
        localPerm = 4
        
        if x > 0 and grid[y][x-1] == 1:
            localPerm -= 1
            if self.checked[y][x-1] == 0:
                self.checked[y][x-1] = 1
                self.recurseIsland(grid,x-1,y)
                
        if y > 0 and grid[y-1][x] == 1:
            localPerm -= 1
            if self.checked[y-1][x] == 0:
                self.checked[y-1][x] = 1
                self.recurseIsland(grid,x,y-1)
                
        if x < len(grid[0])-1 and grid[y][x+1] == 1:
            localPerm -= 1
            if self.checked[y][x+1] == 0:
                self.checked[y][x+1] = 1
                self.recurseIsland(grid,x+1,y)
                
        if y < len(grid)-1 and grid[y+1][x] == 1:
            localPerm -= 1
            if self.checked[y+1][x] == 0:
                self.checked[y+1][x] = 1
                self.recurseIsland(grid,x,y+1)
        
        self.perm += localPerm