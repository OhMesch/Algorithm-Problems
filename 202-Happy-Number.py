# Problem: Given an integer
# Return: Whether or not the integer is a happy number
'''
A happy number is a number defined by the following process: 
Starting with any positive integer, 
replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=[]
        while n not in seen:
            temp=0
            seen.append(n)
            for elm in str(n):
                temp+=int(elm)**2
            if temp == 1:
                return(True)
            n=temp
        return(False)