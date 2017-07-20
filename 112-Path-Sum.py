# Problem: Given a binary tree
# Return: Each level of the tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return(False)
        boolLeafs = list()
        self.helper(root,sum,0,boolLeafs)
        if any(boolLeafs):
            return(True)
        else:
            return(False)
        
    def helper(self,root,target,pathSum,arr):
        """
        :type root: TreeNode
        :type depth: int
        :rtype: int
        """
        pathSum += root.val
        if root.left:
            self.helper(root.left,target,pathSum,arr)
        if root.right:
            self.helper(root.right,target,pathSum,arr)
        if (not root.left) and (not root.right): 
            if (pathSum == target):
                arr.append(True)
            else:
                arr.append(False)
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

t4 = None

print(driver.hasPathSum(t1,3))
print(driver.hasPathSum(t2,7))
print(driver.hasPathSum(t3,18))
print(driver.hasPathSum(t4,5))