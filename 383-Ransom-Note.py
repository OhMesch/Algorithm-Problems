# Problem: Given an array of numbers representing max jump length from the current index
# Return: True if the end of the array can be reached from the start or false if it cannot

class Solution(object):
	def canJump(self, n,l):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		CHANGE CLASS and and and and 
		mag = {}
		for char in l:
			if char in mag:
				mag[char] += 1
			else:
				mag[char] = 1
		for char in n:
			if char in mag:
				if mag[char] > 0:
					mag[char] -=1
				else:
					return(False)
			else:
				return(False)
		return(True)


driver = Solution()
a1,b1 = 'a','b'
a2,b2 = 'aa','ab'
a3,b3 = 'aa','aab'

print('\n')
print('Note:',a1,'\nLetters:',b1,'\nProgram vs Expected sol:\n',driver.canJump(a1,b1),'\n False\n')
print('Note:',a2,'\nLetters:',b2,'\nProgram vs Expected sol:\n',driver.canJump(a2,b2),'\n False\n')
print('Note:',a3,'\nLetters:',b3,'\nProgram vs Expected sol:\n',driver.canJump(a3,b3),'\n True\n')
