class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        runningSum = num1 = num2 = index =leftpara = 0
        array = []
        para = {}
        s.replace(' ','')

        while index < len(s):
            itera = True
            currentNum=[]
            if s[index] == '+' or s[index] == '-' or s[index] == '/' or s[index] == '*' or s[index] == '(' or s[index] == ')':
                array.append(s[index])
            else:
                while index < len(s) and self.numberCheck(s[index]):
                    currentNum.append(s[index])
                    index += 1
                    itera = False
                if len(currentNum) > 0:
                    revNum = list(reversed(currentNum))
                    multiNum = 0
                    for j in range(len(currentNum)):
                        multiNum += int(revNum[j]) * (10**j)
                    array.append(str(multiNum))
            if itera:
                index+=1

        print(array)

        for k in range(len(array)):
            if array[k] == '(':
                leftPara = k
            if array[k]==')':
                simplify = array[leftPara+1:k]
                newS = ''
                for elm in simplify:
                    newS += elm
                # replace = self.calculate(newS)
                tempArr = array[0:leftPara]
                tempArr.append(str('replace'))
                for elm in array[k+1:]:
                    tempArr.append(elm)
                print(tempArr)



    def numberCheck(self,s):
        """
        :type s: unknown
        :rtype: bool
        """
        try:
            float(s)
            return(True)
        except ValueError:
            return(False)

driver = Solution()

t1 = "1+1"
t2 = "2-1 + 2 "
t3 = "(1+(4+5+2)-3)+(6+8)"
t4 = "(100+1)*(12-11)"

print('\n')
print(' Equation:',t1, '\n', driver.calculate(t1),"\n Answer: 2\n")
print(' Equation:',t2, '\n', driver.calculate(t2),"\n Answer: 3\n")
print(' Equation:',t3, '\n', driver.calculate(t3),"\n Answer: 23\n")
print(' Equation:',t4, '\n', driver.calculate(t4),"\n Answer: 101\n")