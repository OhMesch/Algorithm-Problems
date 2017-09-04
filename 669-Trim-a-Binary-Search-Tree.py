# Problem: Given a binary search tree and the lowest and highest boundaries as L and R
# Return: the tree so that all its elements lies in [L, R] (R >= L)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root:
            if root.val > R:
                return(self.trimBST(root.left,L,R))
            elif root.val < L:
                return(self.trimBST(root.right,L,R))
            else:
                root.right = self.trimBST(root.right,L,R)
                root.left = self.trimBST(root.left,L,R)
                return(root)