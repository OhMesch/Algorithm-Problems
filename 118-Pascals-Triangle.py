'''
Problem:
Given numRows, generate the first numRows of Pascal's triangle.
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        full_triangle = []
        for row in range(numRows):
            if row == 0:
                full_triangle.append([1])
                continue
            curr_row = [1]
            prev_row = full_triangle[row-1]
            for i in range(1,len(prev_row)):
                curr_row.append(prev_row[i]+prev_row[i-1])
            curr_row.append(1)
            full_triangle.append(curr_row)
        return(full_triangle)