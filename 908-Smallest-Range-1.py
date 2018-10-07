class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        minVal = A[0]
        maxVal = A[0]

        for val in A:
            if val < minVal:
                minVal = val
            if val > maxVal:
                maxVal = val

        if(maxVal - minVal <= 2*K):
            return(0)
        else:
            return(maxVal - minVal - 2*K)

driver = Solution()
print("1:")
print("**",driver.smallestRangeI([1],0))
print("-- 0")

print("2:")
print("**",driver.smallestRangeI([0, 10], 2))
print("-- 6")

print("3:")
print("**",driver.smallestRangeI([1,3,6],3))
print("-- 0")