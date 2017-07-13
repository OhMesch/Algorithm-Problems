# Problem: Given an integer
# Return: Fizz for numbers divisible by 3 and buzz for numbers divisible by 5

class Solution(object):
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		sol = []
		for i in range(1,n+1):
			if i %3 == 0 and i % 5 == 0:
				sol.append('FizzBuzz')
			elif i%3 == 0:
				sol.append('Fizz')
			elif i % 5 == 0:
				sol.append('Buzz')
			else:
				sol.append(str(i))
		return(sol)


driver = Solution()
t1 = 30
print('Number:',t1,'Program vs Expected sol:\n',driver.fizzBuzz(t1),'\n ["1","2","Fizz","4","Buzz",	"Fizz",	"7","8","Fizz",	"Buzz",	"11","Fizz","13","14","FizzBuzz"]\n')