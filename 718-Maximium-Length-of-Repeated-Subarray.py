# Problem: Given two integer arrays A and B
# Return: The maximum length of an subarray that appears in both arrays

class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        max_val = 0
        history = [(len(B))*[0] for a in range(len(A))]
        for j in range(len(A)):
            for i in range(len(B)):
                if A[j] == B[i]:
                    if i == 0 or j == 0:
                        history[j][i] = 1
                    else:
                        history[j][i] = history[j-1][i-1]+1
                    if history[j][i] > max_val:
                        max_val=history[j][i]
        return(max_val)


# driver = Solution()
# print(driver.findLength([1,2,3,2,1],[3,2,1,4,7]))
# print(driver.findLength([3,2,1,4,7],[3,2,1,4,7]))
