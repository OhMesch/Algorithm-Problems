# Problem: Given two binary trees
# Return: Whether or not the two trees are equal the same

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p:
            if not q:
                return(True)
            else:
                return(False)
        if not q:
            return(False)

        return(self.helperDFS(p,q))
        
    def helperDFS(self, n1,n2):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if n1.val != n2.val:
            return(False)
        if n1.left:
            if n2.left:
                if not self.helperDFS(n1.left,n2.left):
                    return(False)
            else:
                return(False)
        if n2.left and not n1.left:
            return(False)

        if n1.right:
            if n2.right:
                if not self.helperDFS(n1.right,n2.right):
                    return(False)
            else:
                return(False)
        if n2.right and not n1.right:
            return(False)
        return(True)
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

t5 = TreeNode(2)
t5.right = TreeNode(4)

t6 = TreeNode(2)
t6.left = TreeNode(3)
t6.right = TreeNode(4)

t7 = TreeNode(1)
t7.right = TreeNode(1)


print(driver.isSameTree(t1,t2),'False')
print(driver.isSameTree(t2,t3),'False')
print(driver.isSameTree(t3,t4),'False')
print(driver.isSameTree(t4,t1),'False')
print(driver.isSameTree(t1,t3),'False')
print(driver.isSameTree(t2,t4),'False')
print(driver.isSameTree(t3,t1),'False')
print(driver.isSameTree(t4,t2),'False')
print(driver.isSameTree(t1,t3),'False')
print(driver.isSameTree(t2,t4),'False')
print(driver.isSameTree(t3,t1),'False')
print(driver.isSameTree(t4,t2),'False')
print(driver.isSameTree(t1,t1),'True')
print(driver.isSameTree(t2,t2),'True')
print(driver.isSameTree(t3,t3),'True')
print(driver.isSameTree(t4,t4),'True')
print(driver.isSameTree(t5,t6),'False')
print(driver.isSameTree(t7,t7),'True')