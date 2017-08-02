# Problem: Given a string of mixed upper and lower case leter
# Return: Whether or not the cases are used appropriately

# Rules:
'''
	All letters in this word are capitals, like "USA".
	All letters in this word are not capitals, like "leetcode".
	Only the first letter in this word is capital if it has more than one letter, like "Google".
'''

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper():
            return(True)
        elif word == word.lower():
            return(True)
        elif word == word[0].upper()+word[1:].lower():
            return(True)
        else:
            return(False)

driver = Solution()

t1 = "Test"
t2 = "TEST"
t3 = "teSt"
t4 = "TeSt"
t5 = "test"

print('\n')
print(t1)
print(driver.detectCapitalUse(t1),'True')
print(driver.detectCapitalUse(t2),'True')
print(driver.detectCapitalUse(t3),'False')
print(driver.detectCapitalUse(t4),'False')
print(driver.detectCapitalUse(t5),'True')