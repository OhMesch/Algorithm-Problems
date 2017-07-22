class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        sol = (num+1)*[0]
        sol[1] = 1  
        lastBinary = 1

        for i in range(1,num+1):
            if self.log2(i):
                sol[i] = 1
                lastBinary = i
            else:
                sol[i] = sol[lastBinary]+sol[i-lastBinary]
                print(i,lastBinary)
        return(sol)


    def log2(self,num):
        """
        :type num: int
        :rtype: bool
        """
        if num % 2 != 0:
            return(False)
        while num != 1:
            if num % 2 != 0:
                return(False)
            num /=2
        return(True)



driver = Solution()
t1 = 2
t2 = 5
t3 = 65

print('\n')
print('Number:', t1,'\nProgram vs expected sol\n',driver.countBits(t1),'\n [0,1,1]\n')
print('Number:', t2,'\nProgram vs expected sol\n',driver.countBits(t2),'\n [0,1,1,2,1,2]\n')
print('Number:', t3,'\nProgram vs expected sol\n',driver.countBits(t3),'\n [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,1,2]\n')