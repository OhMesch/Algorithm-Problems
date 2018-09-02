# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.nodeVals = []
        self.trueRoot = None

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.gatherNodesInOrder(root)
        self.buildTree()
        return(self.trueRoot)

    def gatherNodes(self, node):
        if node.left:
            self.gatherNodes(node.left)
        self.nodeVals.append(node.val)
        if node.right:
            self.gatherNodes(node.right)

    def buildTree(self):
        self.trueRoot = TreeNode(self.nodeVals[0])
        prevNode = self.trueRoot
        for i in range(1, len(self.nodeVals)):
            currNode = TreeNode(self.nodeVals[i])
            prevNode.right = currNode
            prevNode = currNode

    def DFS(self, node):
        print(node.val)
        if node.left:
            self.DFS(node.left)
        else:
            print("Left Child Null")
        if node.right:
            self.DFS(node.right)
        else:
            print("Right Child Null")

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

a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(8)
g = TreeNode(1)
h = TreeNode(7)
i = TreeNode(9)

a.left = b
a.right = c
c.right = f
f.left = h
f.right = i

b.left = d
b.right = e
d.left = g
a.left = b
a.left = b

c = Solution()
a = c.increasingBST(a)
c.DFS(a)
# c.BFS(a)