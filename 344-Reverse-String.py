# Problem: Given a string
# Return: THe reversed string

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return(s[::-1])

driver = Solution()

t1 = 'Hello'
print('\n')
print('String',t1, '\nReversed:',driver.reverseString(t1),'\nExpected Answer:','elloH')