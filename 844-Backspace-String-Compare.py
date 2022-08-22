class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        finalSString = self.buildString(S)
        finalTString = self.buildString(T)
        return(bool(finalSString == finalTString))

    def buildString(self,input):
    	r = 0
    	w = 0
    	strLen = len(input)
    	sol = [""] * strLen

    	while input[r] == '#':
    		r+=1

    	while r < strLen:
    		if input[r] == '#':
    			if w >= 0:
	    			w -= 1
	    			sol[w] = ""
    		else:
    			sol[w] = input[r]
    			w+=1
    		r+=1
    	return("".join(sol))


driver = Solution()
print("1 ", driver.backspaceCompare("ab#c","ad#c")," True")
print("2 ", driver.backspaceCompare("ab##","c#d#")," True")
print("3 ", driver.backspaceCompare("a##c","#a#c")," True")
print("4 ", driver.backspaceCompare("a#c","b")," False")
print("5 ", driver.backspaceCompare("j##xfix","j###xfix")," True")