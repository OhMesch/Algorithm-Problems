# Given a balanced parentheses string S, compute the score of the string based on the following rule:

#     () has score 1
#     AB has score A + B, where A and B are balanced parentheses strings.
#     (A) has score 2 * A, where A is a balanced parentheses string.


class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        
driver = Solution()

print("1")
print(driver.scoreOfParentheses("()"))
print(1)

print("\n2")
print(driver.scoreOfParentheses("(())"))
print(2)

print("\n3")
print(driver.scoreOfParentheses("()()"))
print(2)

print("\n")
print(driver.scoreOfParentheses("(()(()))"))
print(1)