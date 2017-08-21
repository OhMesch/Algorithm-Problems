# Problem: Given a binary tree
# Return: check if it's possible to partition the tree to two trees which have the equal sum of values 
# 		  after removing exactly one edge on the original tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        if not root.right and not root.left:
            return False
        global sums
        sums = set()
        total = self.sumTree(root)
        return(total / 2 in sums)

    def sumTree(self, curr):
    	global sums
    	left,right = curr.left,curr.right
    	if left and right:
    		nodeSum = self.sumTree(left)+self.sumTree(right)+curr.val
    		sums.add(nodeSum)
    		return(nodeSum)
    	elif left or right:
    		nextNode = left or right
    		nodeSum = self.sumTree(nextNode)+curr.val
    		sums.add(nodeSum)
    		return(nodeSum)
    	else:
    		sums.add(curr.val)
    		return(curr.val)

driver = Solution()

print('\n')

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

t4 = TreeNode(1)
t4.left = TreeNode(3)
t4.right = TreeNode(2)
t4.left.left = TreeNode(5)
t4.right.right = TreeNode(9)
t4.right.right.right = TreeNode(7)
t4.left.left.left = TreeNode(6)

t5 = TreeNode(5)
t5.left = TreeNode(10)
t5.right = TreeNode(10)
t5.right.right = TreeNode(3)
t5.right.left = TreeNode(2)

t6 = TreeNode(0)
t6.left = TreeNode(1)
t6.right = TreeNode(1)

t7 = TreeNode(0)

print(driver.checkEqualTree(t1))
print(driver.checkEqualTree(t2))
print(driver.checkEqualTree(t3))
print(driver.checkEqualTree(t4))
print(driver.checkEqualTree(t5))
print(driver.checkEqualTree(t6))
print(driver.checkEqualTree(t7))