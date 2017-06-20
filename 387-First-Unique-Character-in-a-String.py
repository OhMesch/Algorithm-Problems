# Problem Statement: Given a string of lower-case letters
# Return the index of the first non-repeating letter

class Solution(object):
	def firstUniqChar(self, s):
		failed = []
		unique = {}
		solutions =[]
		for index in range(len(s)):
			if s[index] in unique:
				failed.append(s[index])
				unique.pop(s[index],None)
				continue
			if s[index] in failed:
				continue
			unique[s[index]] = index
		if any(unique):
			for k,v in unique.items():
				solutions.append(v)
			return(min(solutions))
		else:
			return(-1)

		



driver = Solution()
t1 = 'leetcode'
t2 = 'loveleetcode'
t3 = 'ooollvv'

print('\n')
print('\n',driver.firstUniqChar(t1),'answer=0\n')
print('\n',driver.firstUniqChar(t2),'answer=2\n')
print('\n',driver.firstUniqChar(t3),'answer=-1\n')