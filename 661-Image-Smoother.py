# Problem: Given a 2D array representing the gray scale of an image
# Return: The average gray scale (rounded down) of all 8 surrounding cells and itself

class Solution(object):
    def newInteger(self, M):
        """
        :type M: int
        :rtype: int
        """
        output = [[0 for x in range(len(M[0]))] for y in range(len(M))]
        for y in range(len(M)):
            for x in range(len(M[0])):
                right = False
                left = False
                up = False
                down = False

                total = M[y][x]
                num = 1
                
                if x+1 < len(M[0]):
                    right = True
                if x-1 >= 0:
                    left = True
                if y+1 < len(M):
                    down = True
                if y-1 >=0:
                    up = True

                if right:
                    total += M[y][x+1]
                    num += 1
                    if up:
                        total+=M[y-1][x+1]
                        num+=1
                    if down:
                        total+=M[y+1][x+1]
                        num+=1
                if left:
                    total += M[y][x-1]
                    num += 1
                    if up:
                        total+=M[y-1][x-1]
                        num+=1
                    if down:
                        total+=M[y+1][x-1]
                        num+=1
                if up:
                    total+=M[y-1][x]
                    num+=1
                if down:
                    total+=M[y+1][x]
                    num+=1
                output[y][x] = (total//num)
        return(output)

driver = Solution()

print('\n')

print('1')
print('**',driver.newInteger([[1,1,1],[1,0,1],[1,1,1]]))
print("-- [[0, 0, 0], [0, 0, 0], [0, 0, 0]]\n")