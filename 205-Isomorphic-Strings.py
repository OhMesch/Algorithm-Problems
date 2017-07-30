# Problem: Given strings s and t
# Return: True if the strings are isomorphic
# Isomorphic: The characters in s can be replaced to get t. All occurence of a character
# Must be replaced with anouther character while preserving the order

class Solution(object):
    def isIsomorphic(self,s,t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        bound = set()
        charEquiv = {}
        for i in range(len(s)):
        	if s[i] not in charEquiv:
        		if t[i] in bound:
        			return(False)
        		charEquiv[s[i]] = t[i]
        		bound.add(t[i])
        	else:
        		if charEquiv[s[i]] != t[i]:
        			return(False)
        return(True)

driver = Solution()
s1,t1 = 'egg','add'
s2,t2 = 'foo','bar'
s3,t3 = 'paper','title'
s4,t4 = 'purr','pahh'
s5,t5 = 'parputt','purpple'
s6,t6 = 'e  d','addj'
s7,t7 = 'the car','and zoo'
s8,t8 = 'the bcc','and zoo'

print('\n')
print(' %s\n %s\n' % (s1,t1),driver.isIsomorphic(s1,t1),'True\n')
print(' %s\n %s\n' % (s2,t2),driver.isIsomorphic(s2,t2),'False\n')
print(' %s\n %s\n' % (s3,t3),driver.isIsomorphic(s3,t3),'True\n')
print(' %s\n %s\n' % (s4,t4),driver.isIsomorphic(s4,t4),'True\n')
print(' %s\n %s\n' % (s5,t5),driver.isIsomorphic(s5,t5),'False\n')
print(' %s\n %s\n' % (s6,t6),driver.isIsomorphic(s6,t6),'True\n')
print(' %s\n %s\n' % (s7,t7),driver.isIsomorphic(s7,t7),'False\n')
print(' %s\n %s\n' % (s8,t8),driver.isIsomorphic(s8,t8),'True\n')