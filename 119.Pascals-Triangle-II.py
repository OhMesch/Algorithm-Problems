# Problem: Given an index k, return the kth row of the Pascal's triangle.

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        curr_row = [1]
        for row in range(rowIndex):
            prev_row = curr_row
            curr_row = [1]
            for i in range(1,len(prev_row)):
                curr_row.append(prev_row[i]+prev_row[i-1])
            curr_row.append(1)
        return(curr_row)