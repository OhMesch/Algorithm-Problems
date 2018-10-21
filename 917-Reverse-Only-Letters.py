class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letterStack = self.getLetterStack(S)
        solArr = []
        for char in S:
            if self.isLetter(char):
                solArr.append(letterStack.pop())
            else:
                solArr.append(char)
        return("".join(solArr))

    def getLetterStack(self, S):
        letterStack = []
        for char in S:
            if self.isLetter(char):
                letterStack.append(char)
        return(letterStack)

    def isLetter(self, letter):
        ascii = ord(letter)
        capital = ascii >= 65 and ascii <= 90
        lower = ascii >= 97 and ascii <= 122
        return(capital or lower)

driver = Solution()
print("1:")
print("**",driver.reverseOnlyLetters("ab-cd"))
print("-- dc-ba")

print("2:")
print("**",driver.reverseOnlyLetters("a-bC-dEf-ghIj"))
print("-- j-Ih-gfE-dCba")

print("3:")
print("**",driver.reverseOnlyLetters('Test1ng-Leet=code-Q!'))
print("-- Qedo1ct-eeLg=ntse-T!")

print("4:")
print("**",driver.reverseOnlyLetters("AaW;c?["))
print("-- cWa;A?[")