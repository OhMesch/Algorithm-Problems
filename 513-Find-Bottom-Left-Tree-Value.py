# Problem: Given a binary tree
# Return: The leftmost bottom leaf

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return(self.findBottomLeftValueFull(root,0,[]))
        #Using optional variables on the basic function causes strange issues.
    def findBottomLeftValueFull(self,root,depth,treeArr)
        if ((root.left == None) and (root.right == None) and (depth == 0)):
            return(root.val)
        treeArr.append([root.val,depth])
        if root.left:
            self.findBottomLeftValueFull(root.left,depth+1,treeArr)
        if root.right:
            self.findBottomLeftValueFull(root.right,depth+1,treeArr)
        if depth == 0:
            maxDepth = -1
            for array in treeArr:
                if array[1] > maxDepth:
                    sol = array[0]
                    maxDepth = array[1]
                    print(sol)
            return(sol)

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

print(driver.findBottomLeftValue(t1))
