# Problem: Given a string of words
# Return: The string with each word reversed in order

class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		solution = ''
		s = s.replace(' ',' | ')
		sArr = s.split(' ')
		for word in sArr:
			if word == '|':
				solution += ' '
			else:
				solution += (word[::-1])
		return(solution)

driver = Solution()

t1 = 'Hello this is a test'
print('\n')
print('String',t1, '\nReversed:',driver.reverseWords(t1),'\nExpected Answer:','elloH siht si a tset')