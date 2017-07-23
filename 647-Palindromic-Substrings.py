# Problem: Given a string
# Return: The number of palindromic countSubstrings

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 2:
            if s[0] == s[1]:
                return(3)

        sol = 0
        sol += len(s)

        if len(s) >=3:
            for i in range(1,len(s)):
                if s[i-1] == s[i]:
                    j = i
                    k = i
                    while (j-1)>=0 and k<len(s) and s[j-1] == s[k]:
                        sol+=1
                        j-=1
                        k+=1
                if i < len(s) - 1 and s[i-1] == s[i+1]:
                    k = 1
                    while (i-k)>=0 and (i+k)<len(s) and s[i-k]==s[i+k]:
                        sol+=1
                        k+=1
        return(sol)



driver = Solution()
t1 = 'aaa'
t2 = 'abc'
t3 = 'abccba'
t4 = 'aa'

print('\n')
print(driver.countSubstrings(t1),'6')
print(driver.countSubstrings(t2),'3')
print(driver.countSubstrings(t3),'9')
print(driver.countSubstrings(t4),'3')
