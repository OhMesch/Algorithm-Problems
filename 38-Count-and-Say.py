'''
Problem:
The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string. 
'''

'''
Future work:
Replace getNext with generator
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count_say = '1'
        for i in range(n-1):
            count_say = self.getNext(count_say)
        return(count_say)
    
    def getNext(self,s):
        i = 0
        next_s = ''
        while i < len(s):
            tracking = s[i]
            counter = 0
            while i < len(s) and s[i] == tracking:
                counter += 1
                i += 1
            next_s += (str(counter)) + (str(tracking))
        return(next_s)