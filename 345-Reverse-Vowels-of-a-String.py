class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        if [v for v in vowels if v in s] == []:
            return(s)
        s = list(s)
        solArr = len(s)*[0]
        i,j = 0, len(s) - 1
        while i <= j:
            while j-1 >= 0 and s[j] not in vowels:
                solArr[j] = s[j]
                j-=1
            if s[i] not in vowels:
                solArr[i] = s[i]
                i +=1
            else:
                solArr[i],solArr[j] = s[j],s[i]
                i+=1
                j-=1
        print(solArr)
        print(solArr)
        return(''.join(solArr))

driver = Solution()
t1 = 'Hello'
t2 = '.a'
t3 = '   cat'

print('\n')
print('String',t1, '\nReversed:',driver.reverseVowels(t1),'\nExpected Answer:','Holle')
print('String',t2, '\nReversed:',driver.reverseVowels(t2),'\nExpected Answer:','.a')
print('String',t3, '\nReversed:',driver.reverseVowels(t3),'\nExpected Answer:','   cat')