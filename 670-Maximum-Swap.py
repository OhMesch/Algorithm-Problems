# Problem: Given a non-negative integer
# Return: The maximum integer possible by swapping any two values once

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums=[int(x) for x in list(str(num))]
        numsSorted=sorted(nums,reverse=True)
        if nums == numsSorted:
            return(int(''.join([str(x) for x in nums])))
        
        for j in range(len(nums)):
            if nums[j] != numsSorted[j]:
                for i in range(len(numsSorted)-1,j,-1):
                    if nums[i] == numsSorted[j]:
                        nums[i],nums[j] = nums[j],nums[i]
                        return(int(''.join([str(x) for x in nums])))