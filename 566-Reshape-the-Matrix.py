# Problem: You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
# Return: The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return(nums)
        
        restruct = [[0 for x in range(c)] for y in range(r)]
        
        reorganize=[]
        for row in range(len(nums)):
            for col in range(len(nums[0])):
                reorganize.append(nums[row][col])
        
        counter=0
        for row in range(len(restruct)):
            for col in range(len(restruct[0])):
                restruct[row][col] =reorganize[counter]
                counter+=1
                
        return(restruct)