# Problem: Given a matrix representing an island
# Return: The perimeter of island

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        #Clean solution
        # return(list(set(nums1)&set(nums2)))

        #Fast solution
        d = {}
        sol = []
        for elm in nums1:
            if elm not in d:
                d[elm] = 1
        for elm in nums2:
            if d.get(elm,0) == 1:
                d[elm] =2
                sol.append(elm)    
        return(sol)