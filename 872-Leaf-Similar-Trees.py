'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''

'''
Both of the given trees will have between 1 and 100 nodes.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.leaves = [[],[]]
        
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.gatherLeafs(root1, 0)
        self.gatherLeafs(root2, 1)
        return(self.leaves[0]==self.leaves[1])
    
    def gatherLeafs(self, root, idx):
        if root.left:
            self.gatherLeafs(root.left, idx)
        if root.right:
            self.gatherLeafs(root.right, idx)
        if not root.left and not root.right:
            self.leaves[idx].append(root.val)