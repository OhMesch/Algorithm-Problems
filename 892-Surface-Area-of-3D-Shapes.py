# On a N * N grid, we place some 1 * 1 * 1 cubes.

# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

# Return the total surface area of the resulting shapes.

# If the input is [[2]], it means that N = 1, and grid[0][0] = 2.

# If the input is [[1,2],[3,4]], it means that N = 2, and grid[0][0] = 1, grid[0][1] = 2, grid[1][0] = 3, grid[1][1] = 4;
# The grid[][] will look like:
# 1 2
# 3 4

# If the input is [[1,1,1],[1,0,1],[1,1,1]]
# The grid[][] will look like:
# 1 1 1
# 1 0 1
# 1 1 1

# Also appearently the bricks are floating in space because the grid does not count

class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        surface = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                surface+=self.calcTowerArea(grid[j][i])

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if y+1 < len(grid):
                    surface-=2*min(grid[y][x],grid[y+1][x])
                if x+1 < len(grid[0]):
                    surface-=2*min(grid[y][x],grid[y][x+1])

        return(surface)


    def calcTowerArea(self, blocks):
        if blocks != 0:
            return(4*(blocks)+2)
        else:
            return(0)



driver = Solution()

print("0:")
print("**",driver.surfaceArea([[2]]))
print("-- 10")


print("1:")
print("**",driver.surfaceArea([[1,2],[3,4]]))
print("-- 34")

print("2:")
print("**",driver.surfaceArea([[1,0],[0,2]]))
print("-- 16")

print("3:")
print("**",driver.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
print("-- 32")

print("4:")
print("**",driver.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))
print("-- 46")