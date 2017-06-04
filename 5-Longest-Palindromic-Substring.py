# Problem Statement:
# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

class Solution(object):
	def longestPalindrome(self, s):
		if len(s) == 1:
			return(s)

		twoAway = s[0]
		oneAway = s[1]
		index = 2
		palidromes = ['']
		prev = frwd = 0

		if s[0] == s[1]:
			palidromes.append(s[0:2])

		if s.replace(s[0],'') =='':
			return(s)

		while index < len(s):
			if s[index] == twoAway:
				frwd = index 
				prev = index - 2

				while(s[frwd] == s[prev]):
					if frwd == len(s) -1 or prev == 0:
						palidromes.append(s[prev:frwd+1])
						break
					else:
						frwd = frwd + 1
						prev = prev - 1
						palidromes.append(s[prev+1:frwd])



			if s[index] == oneAway:
				frwd = index
				prev = index - 1
				while(s[frwd] == s[prev]):
					if frwd == len(s) -1 or prev == 0:
						palidromes.append(s[prev:frwd+1])
						break
					else:
						frwd = frwd + 1
						prev = prev - 1
						palidromes.append(s[prev+1:frwd])
 
			twoAway = oneAway
			oneAway = s[index]
			index += 1

		if len(max(palidromes, key =len)) == 0:
			return(s[0])
		return(max(palidromes, key =len))


driver = Solution()

t1 = "babad"            #aba or bab
t2 = "cbbd"             #bb
t3 = "firecattacdapper" #cattac
t4 = 'a'				# a
t5 = 'cccc'				# cccc
t6 = 'ccccccccccc'		# cccccccccccc
t7 = 'abcb'				# bcb
t8 = 'ccd'				# ccd
t9 = 'abcda'			#a
t10 = 'annakayakracecar'#racecar
t11 = "aaabbbbccccbbbbaaa"


print(driver.longestPalindrome(t1))
print(driver.longestPalindrome(t2))
print(driver.longestPalindrome(t3))
print(driver.longestPalindrome(t4))
print(driver.longestPalindrome(t5))
print(driver.longestPalindrome(t6))
print(driver.longestPalindrome(t7))
print(driver.longestPalindrome(t8))
print(driver.longestPalindrome(t9))
print(driver.longestPalindrome(t10))
print(driver.longestPalindrome(t11))

# tests = []
# tests.append(t1)
# tests.append(t2)
# tests.append(t3)
# print(tests, max(tests))