# Problem: Given an array of non-duplicate numbers

# Return: The maximium binary tree

# The maxiumum binary tree is defined as followed:
    # The root is the maximum number in the array.
    # The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    # The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if not nums:
            return([])
        mVal = max(nums)
        mIndex = nums.index(mVal)
        
        root = TreeNode(mVal)
        left = nums[:mIndex]
        root.left = self.treeHelper(left)
        if mVal != nums[-1]:
            right = nums[mIndex+1:]
            root.right = self.treeHelper(right)
            
        return(root
              )
    def treeHelper(self,arr):
        if not arr:
            return(None)
        
        mVal = max(arr)
        mIndex = arr.index(mVal)
        
        curr = TreeNode(mVal)
        
        left = arr[:mIndex]
        curr.left = self.treeHelper(left)
        
        if mVal != arr[-1]:
            right = arr[mIndex+1:]
            curr.right = self.treeHelper(right)
        
        return(curr)