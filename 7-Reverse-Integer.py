#Problem Statement:
# Reverse digits of an integer.
# Return zero if the number overflows 32-bit

class Solution(object):
	def reverse(self, x):
		
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
		if abs(int(newStr)) > 2147483647:
			return(0)
		return(int(newStr))

driver = Solution()

t1 = 1534236469
t2 = -123
t3 = -2147483648
t4 = 1563847412

print(driver.reverse(t1))
print(driver.reverse(t2))
print(driver.reverse(t3))
print(driver.reverse(t4))