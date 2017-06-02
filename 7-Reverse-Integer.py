#Problem Statement:
# Reverse digits of an integer.

class Solution(object):
	def reverse(self, x):
		
		orignalInt = x
		originalStr = str(x)
		newStr = []
		neg = 0

		if x < 0:
			neg = 1
			originalStr = originalStr.replace('-','')

		for digit in originalStr:
			newStr.insert(0,digit)

		if neg ==1:
			newStr.insert(0,'-')

		newStr = ''.join(newStr)
		return(int(newStr))

driver = Solution()

t1 = 123
t2 = -123

print(driver.reverse(t1))
print(driver.reverse(t2))