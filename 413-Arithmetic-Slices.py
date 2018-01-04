class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = len(A)*[0]
        for i in range(2,len(A)):
        	diff = A[i-1]-A[i-2]
        	if A[i] == A[i-2] + 2*diff:
        		dp[i] = dp[i-1] + 1
        return(sum(dp))

driver = Solution()
print('\n')

print("1")
print("**",driver.numberOfArithmeticSlices([1, 2, 3, 4]))
print("-- 3\n")

print("2")
print("**",driver.numberOfArithmeticSlices([1,2,3,4,5,6,8,10,12,14,16,18,20]))
print("-- 31\n")

print("3")
print("**",driver.numberOfArithmeticSlices([1,2,5]))
print("-- 0\n")