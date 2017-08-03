class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        s = list(s)
        i,j = 0, len(s) - 1
        while i <= j:
            while j-1 >= 0 and s[j] not in vowels:
                j-=1
            if s[i] not in vowels:
                i +=1
            else:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
        return(''.join(s))

driver = Solution()
t1 = 'Hello'
t2 = '.a'
t3 = '   cat'

print('\n')
print('String',t1, '\nReversed:',driver.reverseVowels(t1),'\nExpected Answer:','Holle')
print('String',t2, '\nReversed:',driver.reverseVowels(t2),'\nExpected Answer:','.a')
print('String',t3, '\nReversed:',driver.reverseVowels(t3),'\nExpected Answer:','   cat')