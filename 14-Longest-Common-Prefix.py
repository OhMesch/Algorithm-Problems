'''
Program:
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return('')
        sol = ''
        index = 0
        curr = ''
        running = True
        while (len(strs[0]) > index) and running:
            curr = strs[0][index]
            for elm in strs:
                if len(elm) <= index or elm[index] != curr:
                    running = False
                    break
            index+=1
            if running:
                sol += curr
        return(sol)