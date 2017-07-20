# Problem: Given a binary tree
# Return: The node value average of each level

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        average = {}
        carrier = self.helper(root,average)
        sol = (len(carrier))*[0]
        for k,v in carrier.iteritems():
            sol[k] = v['sum']/float(v['num'])
        return(sol)
        
    def helper(self,root,carrier,depth=0):
        """
        :type root: TreeNode
        :type depth: int
        :rtype: Dictionary
        """
        if depth not in carrier:
            carrier[depth] = {}
            carrier[depth]['sum'] = root.val
            carrier[depth]['num'] = 1
        else:
            carrier[depth]['sum'] += root.val
            carrier[depth]['num'] += 1
        if root.left:
            self.helper(root.left,carrier,depth+1)
        if root.right:
            self.helper(root.right,carrier,depth+1)
        if depth == 0:
            return(carrier)

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
