# Problem: Given a binary search tree of positive values
# Return: The second minimum value or -1 if none exist

# class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(-1)
        arr=[]
        self.dfsHelper(root,arr)
        if len(arr) < 2:
            return(-1)
        else:
            return(max(arr))
        
    def dfsHelper(self,node,arr):
        left=node.left
        right=node.right
        if len(arr) < 2 and node.val not in arr:
            arr.append(node.val)
        else:
            if node.val < max(arr) and node.val not in arr:
                for i in range(len(arr)):
                    if arr[i]==max(arr):
                        arr[i]=node.val
        if left:
            self.dfsHelper(left,arr)
        if right:
            self.dfsHelper(right,arr)