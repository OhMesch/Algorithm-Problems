# Merge two binary trees

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def mergeTrees(self, t1, t2):
		self.mergeNode(t1,t2)

	def mergeNode(self, t1, t2):
		if t1 == None:
			print(t2.val)
		if t2 == None:
			print(t1.val)
		if t1 != None and t2 != None:
			print(t1.val,t2.val,t1.val+t2.val)
		if t1.left != None:
			self.mergeNode(t1.left,t2.left)
		if t1.right != None:
			self.mergeNode(t1.right,t2.right)
# -----------------------------------------------------------------------
driver = Solution()

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.left = TreeNode(3)
tree.left.left = TreeNode(5)

tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
tree2.left.right = TreeNode(4)
tree2.right.left = TreeNode(7)

driver.mergeNode(tree,tree2)
