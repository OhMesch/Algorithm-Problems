# Merge two binary trees

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def mergeTrees(self, t1, t2):
		arr1 = [None]*10000
		arr2 = [None]*10000
		self.recurse(t1,0,0,arr1)
		self.recurse(t2,0,0,arr2)
		output = arr1 + arr2
		while output[-1] == None:
			del output[-1]
		while output[0] == None:
			del output[0]
		print(arr1,arr2,output)
		return()

	def recurse(self, t1, level,offset,arr):
		# print(t1.val,level,offset)
		# print((2**(level+1)-1) + offset)
		arr[2**(level+1)-1 + offset] = t1.val
		if t1.left != None:
			levl = level +1
			offset = 2*offset
			self.recurse(t1.left,levl,offset,arr)
		if t1.right != None:
			levr = level +1
			offset = offset*2 +1
			self.recurse(t1.right,levr,offset,arr)
driver = Solution()

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.left = TreeNode(3)
tree.left.left = TreeNode(5)
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)
tree2.left.left = TreeNode(4)
tree2.left.right = TreeNode(5)
tree2.right.left = TreeNode(6)
tree2.right.right = TreeNode(7)

driver.mergeTrees(tree,tree2)
