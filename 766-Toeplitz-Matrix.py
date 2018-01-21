# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for y in range(len(matrix)):
            if not self.checkDiag(matrix,y,0):
                return(False)
            
        for x in range(1,len(matrix[0])):
            if not self.checkDiag(matrix,0,x):
                return(False)
            
        return(True)
        
        
    def checkDiag(self, matrix, y, x):
        while y < len(matrix) - 1 and x < len(matrix[0]) - 1:
            if matrix[y][x] != matrix[y+1][x+1]:
                return(False)
            y += 1
            x += 1
        return(True)