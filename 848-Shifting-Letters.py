# We have a string S of lowercase letters, and an integer array shifts.

# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

# Return the final string after all such shifts to S are applied.

# 1 <= S.length = shifts.length <= 20000
# 0 <= shifts[i] <= 10 ^ 9

class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        self.sol = list(S)
        self.cumShift = shifts

        self.calculateCumShift()

        for i,sft in enumerate(self.cumShift):
        	self.shift(i,sft)

        return("".join(self.sol))

    def calculateCumShift(self):
    	for i in range(len(self.cumShift)-2,-1,-1):
    		self.cumShift[i] = self.cumShift[i]+self.cumShift[i+1]

    def shift(self,i,sft):
    	origVal = ord(self.sol[i]) - 97
    	newVal = (origVal + sft) % 26
    	self.sol[i] = chr(newVal+97)

driver = Solution()
print("1")
print(driver.shiftingLetters("abc",[3,5,9]))
print("rpl\n")

print("2")
print(driver.shiftingLetters("zz",[1,1]))
print("ba\n")