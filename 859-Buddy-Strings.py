class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        swaps = 0
        dictA = self.createDict(A)
        dictB = self.createDict(B)
        correctBits = dictA == dictB
        if not correctBits:
            return(False)

        for i in range(len(A)):
            if A[i] != B[i]:
                if swaps:
                    return(False)
                else:
                    swaps += 1
        
        return(swaps == 1)

    def createDict(self,string):
        returnDict = dict()
        for char in string:
            returnDict[char] = returnDict.get(char,0) + 1
        return(returnDict)

driver = Solution()

print("1")
print(driver.buddyStrings("ab","ba"))
print("True")

print("\n2")
print(driver.buddyStrings("ab","ab"))
print("False")

print("\n3")
print(driver.buddyStrings("aa","aa"))
print("True")

print("\n4")
print(driver.buddyStrings("aaaaaaabc","aaaaaaacb"))
print("True")

print("\n5")
print(driver.buddyStrings("","aa"))
print("False")

print("\n6")
print(driver.buddyStrings("",""))
print("False")

print("\n7")
print(driver.buddyStrings("abc","bca"))
print("False")