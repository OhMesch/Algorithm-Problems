# Problem: Given two strings
# Return: Whether or not the strings are anagrams

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return(False)
        return(sorted(s) == sorted(t))