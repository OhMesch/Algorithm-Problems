# Problem:
# Given an integer, convert it to a roman numeral.
# Max integer would be 3999

class Solution(object):
    def intToRoman(self, num):
        roman = []
        while num != 0:
        	if (num - 1000) >= 0:
        		roman.append('M')
        		num = num - 1000
        	elif (num - 900) >= 0:
        		roman.append('CM')
        		num = num - 900
        	elif (num - 500) >= 0:
        		roman.append('D')
        		num = num - 500        		
        	elif (num - 400) >= 0:
        		roman.append('CD')
        		num = num - 400
        	elif (num - 100) >= 0:
        		roman.append('C')
        		num = num - 100
        	elif (num - 90) >= 0:
        		roman.append('XC')
        		num = num - 90
        	elif (num - 50) >= 0:
        		roman.append('L')
        		num = num - 50
        	elif (num - 40) >= 0:
        		roman.append('XL')
        		num = num - 40
        	elif (num - 10) >= 0:
        		roman.append('X')
        		num = num - 10
        	elif (num - 9) >= 0:
        		roman.append('IX')
        		num = num - 9
        	elif (num - 5) >= 0:
        		roman.append('V')
        		num = num - 5
        	elif (num - 4) >= 0:
        		roman.append('IV')
        		num = num - 4
        	elif (num - 1) >= 0:
        		roman.append('I')
        		num = num - 1
        romanAns = ''.join(roman)
        return(romanAns)

# driver = Solution()

# t1 = 4
# t2 = 19
# t3 = 50
# t4 = 3380
# t5 = 2559
# t6 = 2049
# t7 = 1949

# print(t1,driver.intToRoman(t1),'IV')
# print(t2,driver.intToRoman(t2),'XIX')
# print(t3,driver.intToRoman(t3),'L')
# print(t4,driver.intToRoman(t4),'MMMCCCLXXX')
# print(t5,driver.intToRoman(t5),'MMDLIX')
# print(t6,driver.intToRoman(t6),'MMDLIX')
# print(t7,driver.intToRoman(t7),'MCMXLIX')