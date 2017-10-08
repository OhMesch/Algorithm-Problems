'''
Problem: 
Given a positive integer, check whether it has alternating bits or not.
'''

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = "{0:b}".format(n)
        for i in range(1,len(binary)):
            if binary[i-1]==binary[i]:
                return(False)
        return(True)