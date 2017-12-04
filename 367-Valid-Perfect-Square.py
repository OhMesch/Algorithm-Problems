# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt. 

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 1
        while n*n != num and n*n < num:
            n+=1
        return(n*n == num)