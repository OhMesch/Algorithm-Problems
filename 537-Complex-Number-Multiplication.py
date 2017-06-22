# Problem Statement: Given two complex numbers
# Return their product

# Accepted solution

class Solution(object):
	def complexNumberMultiply(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		
		aR,aI = a.split('+')
		bR,bI = b.split('+')

		aI = aI[0:-1]
		bI = bI[0:-1]

		realSol = int(aR)*int(bR)-int(aI)*int(bI)
		imgSol = int(aI)*int(bR)+int(bI)*int(aR)
		
		return(str(realSol)+'+'+str(imgSol)+'i')		

# driver = Solution()

# print('\n')
# print(driver.complexNumberMultiply("1+-1i", "1+-1i"),'answer = 0+-2i')
# print(driver.complexNumberMultiply("0+0i", "0+0i"),'answer = 0+0i')
# print(driver.complexNumberMultiply("3+4i", "3+-4i"),'answer = 25+0i')
# print(driver.complexNumberMultiply("3+2i", "1+4i"),'answer = -5+14i')
# print(driver.complexNumberMultiply("1+4i", "5+1i"),'answer = 1+21i')
# print(driver.complexNumberMultiply("4+1i", "7+-3i"),'answer = 31+-5i')
