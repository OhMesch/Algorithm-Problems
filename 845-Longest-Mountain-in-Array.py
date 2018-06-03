class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.arr = A
        self.arrLen = len(self.arr)
        self.sol = 0

        for i in range(1,self.arrLen-1):
            if self.arr[i] > self.arr[i-1] and self.arr[i] > self.arr[i+1]:
                self.updateSol(1+self.leftCount(i)+self.rightCount(i))

        return(self.sol)

    def leftCount(self,i):
        len = 0

        while i > 0 and self.arr[i-1] < self.arr[i]:
            len+=1 
            i -= 1

        return(len)

    def rightCount(self,i):
        len = 0

        while i < self.arrLen-1 and self.arr[i+1] < self.arr[i]:
            len+=1 
            i += 1

        return(len)


    def updateSol(self, newPossibleSol):
        if newPossibleSol >=3 and newPossibleSol > self.sol:
            self.sol = newPossibleSol
        


driver = Solution()
print("1: ", driver.longestMountain([2,1,4,7,3,2,5])," 5")
print("2: ", driver.longestMountain([2,2,2])," 0")
print("3: ", driver.longestMountain([0,1,2,3,4,5,4,3,2,1,0])," 11")
print("4: ", driver.longestMountain([48,62,39])," 3")
#print("5 ", driver.longestMountain()," ")