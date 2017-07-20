# Problem: Given a binary tree
# Return: The most commonly occuring subtree sums

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return([])
        dictionary = {"maxCount":0}
        self.helperDFS(root,dictionary)
        mc = dictionary["maxCount"]
        del dictionary["maxCount"]
        valKeys = (list(zip(dictionary.values(),dictionary.keys())))
        return([k for (v,k) in valKeys if v == mc])

    def helperDFS(self, root,counter):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root.left:
            self.helperDFS(root.left,counter)
            root.val += root.left.val

        if root.right:
            self.helperDFS(root.right,counter)
            root.val += root.right.val

        if root.val in counter:
            counter[root.val] += 1
        else:
            counter[root.val] = 1
        if counter[root.val] > counter["maxCount"]:
                counter["maxCount"] = counter[root.val]
        
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

t4 = None

t5 = TreeNode(2)
t5.right = TreeNode(4)

t6 = TreeNode(2)
t6.left = TreeNode(3)
t6.right = TreeNode(4)

t7 = TreeNode(1)
t7.right = TreeNode(1)

t8 = TreeNode(5)
t8.left = TreeNode(2)
t8.right = TreeNode(-5)


print(driver.findFrequentTreeSum(t1))
print(driver.findFrequentTreeSum(t2))

print(driver.findFrequentTreeSum(t8))
