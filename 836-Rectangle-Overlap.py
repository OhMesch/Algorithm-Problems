# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

# Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

# Given two (axis-aligned) rectangles, return whether they overlap.

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        recCompletelyBelow = rec2[3] <= rec1[1]
        recCompletelyLeft = rec2[2] <= rec1[0]
        recCompletelyAbove = rec2[1] >= rec1[3]
        recCompleteRight = rec2[0] >= rec1[2]

        return(not(recCompleteRight or recCompletelyAbove or recCompletelyLeft or recCompletelyBelow))


unitTester = Solution()
assert(unitTester.isRectangleOverlap([0,0,2,2],[1,1,3,3]) == True)
assert(unitTester.isRectangleOverlap([0,0,1,1],[1,0,2,1]) == False)
assert(unitTester.isRectangleOverlap([7,8,13,15],[10,8,12,20]) == True)
assert(unitTester.isRectangleOverlap([0,0,1,1],[0,1,1,2]) == False)
assert(unitTester.isRectangleOverlap([2,17,6,20],[3,8,6,20]) == True)