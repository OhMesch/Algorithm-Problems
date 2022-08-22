# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.
# What is the most number of chunks we could have made?
# Note:

#     arr will have length in range [1, 10].
#     arr[i] will be a permutation of [0, 1, ..., arr.length - 1]

class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

driver = Solution()

print(1)
print('**',driver.Solution([4,3,2,1,0]))
print('-- 1\n')

print(2)
print('**',driver.Solution([1,0,2,3,4]))
print('-- 4\n')