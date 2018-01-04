class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start = 0
        curr_len = 0
        i = 2
        sum = 0

        while i < len(A):
        	if curr_len == 0:
        		diff = A[start+1]-A[start]
        	
        	if A[i] == A[i-1] + diff:
        		if curr_len == 0:
        			curr_len = 3
        		else:
        			curr_len += 1
        	else:
        		start = i-1
        		if curr_len:
        			sum += self.triNumber(curr_len-2)
        			curr_len = 0

        	i += 1

        if curr_len:
        	sum += self.triNumber(curr_len-2) 

        return(sum)

    
    def triNumber(self, num):
    	return(int(num*(num+1)/2))

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