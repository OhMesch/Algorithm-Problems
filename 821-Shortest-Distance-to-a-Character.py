# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

class Solution:
    def __init__(self):
        self.inString = None
        self.target = None

    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        self.inString = S
        self.target = C
        self.sol = [20000] * len(self.inString)

        self.iterateForwardAndInializeSolution()
        self.iteratBackwardsAndCompare()

        return(self.sol)

    def iterateForwardAndInializeSolution(self):
        lastTargetIndex = None
        for i,char in enumerate(self.inString):
            if char == self.target:
                self.sol[i] = 0
                lastTargetIndex = i
            elif lastTargetIndex != None:
                self.sol[i] = i - lastTargetIndex

    def iteratBackwardsAndCompare(self):
        lastTargetIndex = None
        for i in range(len(self.inString)-1,-1,-1):
            char = self.inString[i]
            if char == self.target:
                lastTargetIndex = i
            elif lastTargetIndex != None:
                self.sol[i] = min(self.sol[i],lastTargetIndex-i)




unitTester = Solution()
print("\n1")
print("**", unitTester.shortestToChar("loveleetcode","e"))
print("-- [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]")

unitTester = Solution()
print("\n2")
print("**", unitTester.shortestToChar("e     s","e"))
print("-- [0, 1, 2, 3, 4, 5, 6]")