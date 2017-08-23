class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        global d
        if not root:
            return False
        d = {}
        return(bool(self.targetDFS(root,k)))
    
    def targetDFS(self,curr,target):
        global d
        left,right = curr.left,curr.right
        if curr.val in d:
            return True
        elif target-curr.val not in d:
            d[target-curr.val] = curr.val
        if left:
            if self.targetDFS(left,target):
                return True
        if right:
            if self.targetDFS(right,target):
                return True