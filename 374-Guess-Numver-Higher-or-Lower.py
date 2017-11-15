'''
Problem:
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        
        mid = (right+left)//2
        idea = guess(mid)
        print(idea)
        
        while idea:
            idea = guess(mid)
            if idea == -1:
                right = mid
            elif idea == 1:
                left = mid + 1
            mid = (right+left)//2
            
        return(mid)