# Problem:
# Given a string of (, ), {, }, [, and ]
# Determing if the input string is valid

class Solution(object):
    def isValid(self, s):
        op = ['(','{','[']
        cl = [')','}',']']
        ongoing = []

        if s[0] in cl or s[-1] in op:
        	return(False)

        for index in range(3):
        	if s.count(op[index]) != s.count(cl[index]):
        		return(False)

        for para in s:
        	if para in op:
        		ongoing.append(para)
        	if para in cl:
        		prevPara = ongoing.pop()
        		for index in range(3):
        			if para == cl[index] and prevPara != op[index]:
        				return(False)

        return(True)

driver = Solution()
t1 = '()'
t2 = '({[]})'
t3 = '(]'
t4 = '([)]'
t5 = '}{'
t6 = '([{'
t7 = '([{}'

print(t1,driver.isValid(t1))
print(t2,driver.isValid(t2))
print(t3,driver.isValid(t3))
print(t4,driver.isValid(t4))
print(t5,driver.isValid(t5))
print(t6,driver.isValid(t6))
print(t7,driver.isValid(t7))

array = ['a','b','c','d']

array.reverse()
print(array.pop())
print(array.pop())