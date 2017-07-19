# Merge two binary trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 == None:
            return(None)
        if t2 == None:
            return(t1)
        if t1 == None:
            return(t2)
        t1.val = t1.val + t2.val
        if t2.right != None and t1.right != None:
            t1.right = self.mergeTrees(t1.right,t2.right)
        if t2.left != None and t1.left != None:
            t1.left = self.mergeTrees(t1.left,t2.left)
        if t1.left == None and t2.left != None:
            t1.left = t2.left
        if t1.right == None and t2.right != None:
            t1.right = t2.right
        return(t1)
