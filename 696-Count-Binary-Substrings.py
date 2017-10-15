'''
Problem:
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
'''

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        sol = 0
        curr_count = 1
        prev_count = 0
        for i in range(1,len(s)):
        	if s[i] == s[i-1]:
        		curr_count+=1
        	else:
        		sol += min(curr_count,prev_count)
        		prev_count = curr_count
        		curr_count = 1
        sol += min(curr_count,prev_count)
       	return(sol)



driver = Solution()
print('\n')

print('0')
print('**',driver.countBinarySubstrings("00110011"))
print('-- 6')

print('1')
print('**',driver.countBinarySubstrings("10101"))
print('-- 4')

print('2')
print('**',driver.countBinarySubstrings("0011001100110011"))
print('-- 14')

print('3')
print('**',driver.countBinarySubstrings("00110011001100110"))
print('-- 15')

print('4')
print('**',driver.countBinarySubstrings("00110"))
print('-- 3')