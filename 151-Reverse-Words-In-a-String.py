class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return(" ".join(s.split()[::-1]))

driver = Solution()

print("\n")

print("1")
print("**",driver.reverseWords("This is a test"))
print("-- test a is This\n")

print("2")
print("**",driver.reverseWords("the sky is blue"))
print("-- blue is sky the\n")

print("3")
print("**",driver.reverseWords("   lots  of      spaces      "))
print("-- spaces of lots\n")