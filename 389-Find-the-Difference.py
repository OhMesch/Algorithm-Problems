'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        baseline = {}
        compare = {}
        for char in s:
        	baseline[char] = baseline.get(char,0)+1

        for char in t:
        	if char not in baseline:
        		return(char)
        	else:
        		get_val = compare.get(char,0)
        		if baseline[char] <= get_val:
        			return(char)
        		compare[char] = get_val+1

driver = Solution()
print('\n')

print("1")
print('**',driver.findTheDifference("abcd","abcde"))
print('-- e')