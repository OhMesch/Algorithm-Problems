# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other
# The rest of the numbers do not rotate to any other number.

# Now given a positive number N, how many numbers X from 1 to N are good?

class Solution:
    def __init__(self):
        self.cannot = set(['3','4','7'])
        self.unique = set(['2','5','6','9'])

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        sol = 0
        for i in range(N+1):
            if self.rotates(str(i)):
                sol += 1

        return(sol)

    def rotates(self, charnum):
        diff = False
        for char in charnum:
            if char in self.cannot:
                return(False)
            if not diff and char in self.unique:
                diff = True
        return(diff)