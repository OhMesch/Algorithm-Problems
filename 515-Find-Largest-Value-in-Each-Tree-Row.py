# Problem: Given a binary tree
# Return: The node value average of each level

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [root]
        tree = []
        sol = []
        max = -float("inf")
        if root == None:
            return([])
        
        while len(queue) > 0:
            newQueue = []
            for elm in queue:
                current = elm
                tree.append(current.val)
                if current.left:
                    newQueue.append(current.left)
                if current.right:
                    newQueue.append(current.right)
            queue = newQueue
            tree.append('|')
        print(tree)
        for elm in tree:
            if elm == '|':
                sol.append(max)
                max = -float("inf")
            elif elm > max:
                max = elm
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

print(driver.largestValues(t1))
