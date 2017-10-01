# Problem: Given a binary tree
# Return: Each level of the tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def DFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root,0)
        
    def helper(self,root,depth):
        """
        :type root: TreeNode
        :type depth: int
        :rtype: int
        """
        print(root.val)
        if root.left:
            self.helper(root.left,depth+1)
        if root.right:
            self.helper(root.right,depth+1)

# -----------------------------------------------------------------------
driver = Solution()

t1 = TreeNode(1)
t1.right = TreeNode(2)
t1.left = TreeNode(3)
t1.left.left = TreeNode(5)

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.left = TreeNode(7)

t3 = TreeNode(1)
t3.left = TreeNode(2)
t3.right = TreeNode(3)
t3.left.left = TreeNode(4)
t3.left.right = TreeNode(5)
t3.right.left = TreeNode(6)
t3.right.right = TreeNode(7)

print(driver.DFS(t1))
print(driver.DFS(t2))
print(driver.DFS(t3))