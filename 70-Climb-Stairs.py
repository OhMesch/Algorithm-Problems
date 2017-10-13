'''
Problem:
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.d = {}
        return(self.climbHelper(n))
        
    def climbHelper(self,n):
        if n == 1:
            return(1)
        elif n == 2:
            return(2)
        if n not in self.d:
            self.d[n] = self.climbHelper(n-1)+self.climbHelper(n-2)
        return(self.d[n])