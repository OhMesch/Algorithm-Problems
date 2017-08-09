# Problem: Given an integer array
# Return: Find the three numbers with the max product and print it


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg=2*[0]
        pos=3*[0]
        if len(nums) == 3:
            return(nums[0]*nums[1]*nums[2])
        for elm in nums:
            if elm > 0:
                if elm > pos[2]:
                    pos[2],pos[1],pos[0] = elm,pos[2],pos[1]
                elif elm > pos[1]:
                    pos[1],pos[0] = elm,pos[1]
                elif elm > pos[0]:
                    pos[0] = elm
            else:
                if elm < neg[0]:
                    neg[0],neg[1] = elm,neg[0]
                elif elm < neg[1]:
                    neg[1] = elm

        return(max((pos[0]*pos[1]*pos[2]),(pos[2]*neg[0]*neg[1])))