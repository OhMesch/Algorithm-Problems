# Problem: Given a secret number, and a guess at the secret number
# Return: The number of correct digits in the right spot, A's
# And: The number of correct digits in an incorreect spot, B's

class Solution(object):
	def getHint(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		counter = {}
		A = B = 0
		for elm in secret:
			if elm in counter:
				counter[elm] +=1
			else:
				counter[elm]=1
		for i in range(len(secret)):
			if secret[i] == guess[i]:
				A+= 1
				if counter[secret[i]] > 0:
					counter[secret[i]]-=1
				else:
					B-=1
			elif guess[i] in secret and counter[guess[i]] > 0:
				counter[guess[i]] -=1
				B+=1
		return("%dA%dB" % (A,B))


driver = Solution()
t1,g1 = "1807","7810"
t2,g2 = "1123","0111"
t3,g3 = "1122","1222"
print('Number and Guess:',t1,g1,'Program vs Expected sol:\n',driver.getHint(t1,g1),'\n 1A3B\n')
print('Number and Guess:',t2,g2,'Program vs Expected sol:\n',driver.getHint(t2,g2),'\n 1A1B\n')
print('Number and Guess:',t3,g3,'Program vs Expected sol:\n',driver.getHint(t3,g3),'\n 3A0B\n')
