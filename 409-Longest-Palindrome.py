'''
Problem:
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.
'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for char in s:
            d[char] = d.get(char,0)+1
        odd = False
        total_even = 0
        
        for v in d.values():
            if v%2 == 0:
                total_even += v
            else:
                odd = True
                if v > 1:
                    total_even += v-1
            
        return(int(odd)+total_even)