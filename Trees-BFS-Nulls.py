# Problem: Given a binary tree
# Return: Each level of the tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def BFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [root]
        tree = []
        if root == None:
            return([])
        
        while len(queue) > 0:
            newQueue = []
            row =[]
            num = False
            for elm in queue:
                if elm == None:
                    row.append(None)
                    newQueue.extend([None,None])
                else:
                    num = True
                    current = elm
                    row.append(current.val)
                    newQueue.append(current.left)
                    newQueue.append(current.right)
            if num == False:
                break
            queue = newQueue
            tree.append(row)
        print(tree)
        
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

t4 = TreeNode(1)
t4.left = TreeNode(3)
t4.right = TreeNode(2)
t4.left.left = TreeNode(5)
t4.right.right = TreeNode(9)
t4.right.right.right = TreeNode(7)
t4.left.left.left = TreeNode(6)

print(driver.BFS(t1))
print(driver.BFS(t2))
print(driver.BFS(t3))
print(driver.BFS(t4))