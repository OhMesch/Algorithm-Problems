# Problem:
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        sol = []

        if len(s) < len(p):
            return(sol)

        key = self.char_count_arr(p)
        
        win_start = 0
        win_end = win_start+len(p)
        window = self.char_count_arr(s[win_start:win_end])

        while win_end < len(s):
            if window == key:
                sol.append(win_start)
            window[ord(s[win_start])-97] -= 1
            window[ord(s[win_end])-97] += 1
            win_start += 1
            win_end +=1

        if window == key:
            sol.append(win_start)

        return(sol)

    def char_count_arr(self, string):
        char_count = 26*[0]
        for char in string:
            char_count[ord(char)-97] += 1
        return(char_count)


driver = Solution()
print('\n')

print('1')
print('**',driver.findAnagrams("cbaebabacd","abc"))
print('-- [0, 6]\n')

print('2')
print('**',driver.findAnagrams("abab","ab"))
print('-- [0, 1, 2]\n')

print('3')
print('**',driver.findAnagrams("a","ab"))
print('-- []\n')

print('4')
print('**',driver.findAnagrams("aaaaaaa","a"))
print('-- [0, 1, 2, 3, 4, 5, 6]\n')