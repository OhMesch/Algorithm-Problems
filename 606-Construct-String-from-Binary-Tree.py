'''
Problem:
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, root):
        self.arr = []
        self.tree2strHelper(root)
        return(''.join(self.arr))

    def tree2strHelper(self, t):
        if not t:
            return
        self.arr.append(str(t.val))
        if t.right and not t.left:
            self.arr.append('()(')
            self.tree2strHelper(t.right)
            self.arr.append(')')
        else:
            if t.left:
                self.arr.append('(')
                self.tree2strHelper(t.left)
                self.arr.append(')')
            if t.right:
                self.arr.append('(')
                self.tree2strHelper(t.right)
                self.arr.append(')')