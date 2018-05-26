# In a string S of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

# The final answer should be in lexicographic order.

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        self.savedChar = None
        self.currIndex = 0
        self.savedIndex = 0
        self.sol = []

        for currChar in S:
            if currChar != self.savedChar:
                self.checkIfGroup()
                self.updateNewChar(currChar)
            self.currIndex += 1
        self.checkIfGroup()

        return(self.sol)

    def checkIfGroup(self):
         if self.currIndex-self.savedIndex >= 3:
            self.sol.append([self.savedIndex,self.currIndex-1])

    def updateNewChar(self,newChar):
        self.savedChar = newChar
        self.savedIndex = self.currIndex




unitTester = Solution()
assert(unitTester.largeGroupPositions("abbxxxxzzy") == [[3, 6]])
assert(unitTester.largeGroupPositions("abc") == [])
assert(unitTester.largeGroupPositions("abcdddeeeeaabbbcd") == [[3, 5], [6, 9], [12, 14]])
assert(unitTester.largeGroupPositions("abbxxxxzzyxxxxx") == [[3, 6], [10, 14]])