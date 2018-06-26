# Let's call an array A a mountain if the following properties hold:
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.A = A
        lenA = len(A)
        leftBound = 1
        rightBound = lenA-2
        i = lenA//2

        currStatus = self.evaluateCurrPosition(i)
        while currStatus != 'mountain':
        	if currStatus == 'downSlope':
        		rightBound = i - 1
        	else:
        		leftBound = i + 1
        	i = (leftBound + rightBound)//2
        	currStatus = self.evaluateCurrPosition(i)

       	return(i)

    def evaluateCurrPosition(self, i):
    	if(self.A[i-1] < self.A[i] and self.A[i] > self.A[i+1]):
    		return('mountain')
    	elif(self.A[i-1] > self.A[i]):
    		return('downSlope')
    	else:
    		return('upSlope')

driver = Solution()
print('1')
print(driver.peakIndexInMountainArray([0,1,0]))
print('1')

print('\n2')
print(driver.peakIndexInMountainArray([0,2,1,0]))
print('1')