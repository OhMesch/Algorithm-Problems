'''
Problem:
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not. 
'''

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=1:
            return(False)
        sum_div = sum([i + num/i for i in range(1,int(math.sqrt(num)+1)) if num%i == 0 and num != i and num/i != num])+1
        return(sum_div==num)