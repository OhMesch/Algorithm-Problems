# Problem Statement: Given a strin of a basic mathmatical expression
# Return: The mathmatical solution

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        array = []
        s = s.replace(' ','')
        splitS = ''

        for char in s:
            if char == '+':
                splitS+=' + '
            elif char == '-':
                splitS+=' - '
            elif char == '*':
                splitS+=' * '
            elif char == '/':
                splitS+=' / '
            elif char == '(':
                if splitS == '':
                    splitS+='( '
                else:
                    splitS+=' ( '
            elif char == ')':
                splitS+=' ) '
            else:
                splitS+=char
        print('Original=',s,'\nString with spaces =',splitS)
        array = splitS.split(' ')
        if array[-1] == '':
            array.pop()

        print(array)

        while len(array) > 1:
            tempArr=[]
            tempArr.append(array[0])
            i=1
            while i <len(array):
                if '(' in array:
                    for i in range(len(array)):
                        if array[i] =='(':
                            leftPara = i
                        elif array[i] == ')':
                            simplify = array[leftPara+1:i]
                            newS = ''
                            for elm in simplify:
                                newS += elm
                            print('repeat string',newS)
                            replace = self.calculate(newS)
                            tempArr = array[0:leftPara]
                                tempArr.append(elm)
                            for elm in array[i+1:]:
                                tempArr.append(elm)
                    print('Former Full', array)
                    print('Abridged',tempArr)
                    array = tempArr

                elif ('*' in array or '/' in array):
                    while i < len(array) and (array[i] == '*' or array[i] == '/'):
                        if i<len(array) and array[i] == '*':
                            num1 = tempArr.pop()
                            tempArr.append(int(num1)*int(array[i+1]))
                            i+=2

                        if i<len(array) and array[i] == '/':
                            num1 = tempArr.pop()
                            tempArr.append(int(num1)/int(array[i+1]))
                            i+=2

                    if i<len(array):
                        tempArr.append(array[i])
                        i+=1

                else:
                    while i < len(array) and (array[i] == '+' or array[i] == '-'):
                        if array[i] == '+':
                            num1 = tempArr.pop()
                            tempArr.append(int(num1)+int(array[i+1]))
                            i+=2
                        elif array[i] == '-':
                            num1 = tempArr.pop()
                            tempArr.append(int(num1)-int(array[i+1]))
                            i+=2
            array = tempArr
        print(tempArr)
        print(array)
        print('recurse')
        
        if len(array) == 1:
            return(int(array[0]))
        else:
            recurseS=''
            for elm in array:
                recurseS+=elm
        return(recurseS)

        # while k < len(array):
        #     if array[k] == '(':
        #         leftPara = k
        #         while
        #         k+=1
        #     if array[k]==')':
                # simplify = array[leftPara+1:k]
                # newS = ''
                # for elm in simplify:
                #     newS += elm
                # replace = self.calculate(newS)
                # tempArr = array[0:leftPara]
                # tempArr.append(replace)
                # for elm in array[k+1:]:
                #     tempArr.append(elm)
        #         array = tempArr
        #         k+=1
        #         #possible continue
        #     if array[k] == '*' or array[k] == '/':
        #         if array[k] == '*':
        #             tempArr = array[:k-1]
        #             tempArr.append(str(int(array[k-1])*int(array[k+1])))
        #             for elm in array[k+2:]:
        #                 tempArr.append(elm)
        #             array = tempArr
        #             k+=1
        #             #possible continue
        #         else:
        #             tempArr = array[:k-1]
        #             tempArr.append(str(int(array[k-1])/int(array[k+1])))
        #                 tempArr.append(elm)
        #             array = tempArr
        #             break
        # print(array)

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
t5 = "12/3-3+4*3"
t6 = "5-3+6-4*2"

print('\n')
print(' Equation:',t1, '\n', driver.calculate(t1),"\n Answer: 2\n")
print(' Equation:',t2, '\n', driver.calculate(t2),"\n Answer: 3\n")
# print(' Equation:',t3, '\n', driver.calculate(t3),"\n Answer: 23\n")
print(' Equation:',t4, '\n', driver.calculate(t4),"\n Answer: 101\n")
print(' Equation:',t5, '\n', driver.calculate(t5),"\n Answer: 13\n")
print(' Equation:',t6, '\n', driver.calculate(t6),"\n Answer: 0\n")