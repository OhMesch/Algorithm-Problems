'''
Problem:

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd")
'''
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        sol = 1
        long_A = A
        while B not in long_A:
            if len(long_A) > len(B):
                return sol+1 if B in (long_A+A) else -1
            long_A+=A
            sol+=1
        return(sol)