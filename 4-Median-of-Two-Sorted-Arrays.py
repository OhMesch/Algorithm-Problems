# Problem: Given two sorted arrays
# Return: The median of the two arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        counter = 0
        prev = [0,0]
        i=0
        j=0
        total = len(nums1)+len(nums2)
        
        if total % 2 == 0:
            mid = total/2+1
            even = True
        else:
            mid = total//2+1
            even = False
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                prev[0],prev[1] = prev[1],nums1[i]
                i+=1
            else:
                prev[0],prev[1] = prev[1],nums2[j]
                j+=1
            counter+=1  
            if counter == mid:
                if even:
                    return(float(sum(prev))/2)
                else:
                    return(prev[1])
        print(i,j)
        while i < len(nums1):
            prev[0],prev[1] = prev[1],nums1[i]
            i+=1
            counter+=1
            if counter == mid:
                if even:
                    return(float(sum(prev))/2)
                else:
                    return(prev[1])
            
        while j < len(nums2):
            prev[0],prev[1] = prev[1],nums2[j]
            j+=1
            counter+=1
            if counter == mid:
                if even:
                    return(float(sum(prev))/2)
                else:
                    return(prev[1])