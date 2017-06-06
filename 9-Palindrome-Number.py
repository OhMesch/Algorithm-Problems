class Solution(object):
	def isPalindrome(self, x):
		number = str(x)
		if number[0] == '-':
			return(False)
		if number.replace(number[0],'') =='':
			return(True)
		if len(number) == 1:
			return(True)

		fwd = 0
		rev = len(number)-1

		if len(number) % 2 == 0:
			# even
			midr = int(len(number)/2)
			for fwd in range(midr):
				if number[fwd] != number[rev]:
					return(False)
				rev -= 1
			return(True)
		else:
			# odd
			mid = int((len(number)-1)/2)
			for fwd in range(mid):
				if number[fwd] != number[rev]:
					return(False)
				rev -= 1
			return(True)

# t1 = 123					#false
# t2 = 123321					#true
# t3 = -123					#false
# t4 = 123123123321321321		#true
# t5 = 44444					#true
# t6 = -4554					#false
# t7 = 5						#true
# t8 = 12345678				#false
# t9 = 1235321				#true

# driver = Solution()
# print('solution 1',driver.isPalindrome(t1))
# print('solution 2',driver.isPalindrome(t2))
# print('solution 3',driver.isPalindrome(t3))
# print('solution 4',driver.isPalindrome(t4))
# print('solution 5',driver.isPalindrome(t5))
# print('solution 6',driver.isPalindrome(t6))
# print('solution 7',driver.isPalindrome(t7))
# print('solution 8',driver.isPalindrome(t8))
# print('solution 9',driver.isPalindrome(t9))