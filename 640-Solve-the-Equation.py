# Problem: Given an algrebra problem involving x,+, and -
# Return: The value of x

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        xCoeff = 0
        rightSideValue = 0
        
        temp = None
        leftSide = True
        neg = False
        for i in range(len(equation)):
            if equation[i] == '=':
                if temp:
                    if (leftSide and neg) or (not leftSide and not neg):
                        rightSideValue += int(temp)
                        temp = None
                    else:
                        rightSideValue -= int(temp)
                        temp = None
                leftSide = False
                neg = False

            elif equation[i] == 'x':
                if (leftSide and neg) or (not leftSide and not neg):
                    if temp:
                        xCoeff-=int(temp)
                        temp = None
                    else:
                        xCoeff-=1
                else:
                    if temp:
                        xCoeff+=int(temp)
                        temp = None
                    else:
                        xCoeff+=1

            elif equation[i] == '+':
                if temp:
                    if (leftSide and neg) or (not leftSide and not neg):
                        rightSideValue += int(temp)
                        temp = None
                    else:
                        rightSideValue -= int(temp)
                        temp = None
                neg = False

            elif equation[i] == '-':
                if temp:
                    if (leftSide and neg) or (not leftSide and not neg):
                        rightSideValue += int(temp)
                        temp = None
                    else:
                        rightSideValue -= int(temp)
                        temp = None
                neg = True
            else:
                if temp:
                    temp+=equation[i]
                else:
                    temp = equation[i]
                if i == len(equation) - 1:
                    if (leftSide and neg) or (not leftSide and not neg):
                        rightSideValue += int(temp)
                    else:
                        rightSideValue -= int(temp)

        print(xCoeff,'x=',rightSideValue)

        if xCoeff != 0:
            return("'x=%d'" % (float(rightSideValue/xCoeff)))
        else:
            if rightSideValue == 0:
                return("'Infinite solutions'")
            else:
                return("'No solution'")
        
driver = Solution()
t1 = "x+5-3+x=6+x-2"
t2 = "x=x"
t3 = "2x=x"
t4 = "2x+3x-6x=x+2"
t5 = "x=x+2"
t6 = "1+1=x"

print('\n')
print(t1)
print("**",driver.solveEquation(t1))
print("-- 'x=2'\n")

print(t2)
print("**",driver.solveEquation(t2))
print("-- 'Infinite solutions'\n")

print(t3)
print("**",driver.solveEquation(t3))
print("-- 'x=0'\n")

print(t4)
print("**",driver.solveEquation(t4))
print("-- 'x=-1'\n")

print(t5)
print("**",driver.solveEquation(t5))
print("-- 'No solution'\n")

print(t6)
print("**",driver.solveEquation(t6))
print("-- 'x=2'\n")