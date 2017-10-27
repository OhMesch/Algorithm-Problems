# Problem: Given a binary tree
# Return: Find the sum of all left leaves


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
        return(self.DSF(root))
        
    def DSF(self,node):
        total = 0
        left = node.left
        right = node.right
        
        if left:
            if self.check_kids(left):
                total += self.DSF(left)
            else:
                total += left.val
                
        if right:
            total += self.DSF(right)
        
        return(total)
        
    def check_kids(self,node):
        return(node.left or node.right)