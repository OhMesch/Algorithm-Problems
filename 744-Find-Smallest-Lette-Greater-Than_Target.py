# Problem:
# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'. 

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for letter in sorted(letters):
            if letter > target:
                return(letter)
        return(letters[0])

# driver = Solution()
# print("\n")

# print("1")
# print("**", driver.nextGreatestLetter(["c", "f", "j"],"a"))
# print("-- 'c'")

# print("2")
# print("**", driver.nextGreatestLetter(["c", "f", "j"],"c"))
# print("-- 'f'")

# print("3")
# print("**", driver.nextGreatestLetter(["c", "f", "j"],"d"))
# print("-- 'f'")

# print("4")
# print("**", driver.nextGreatestLetter(["c", "f", "j"],"g"))
# print("-- 'j'")

# print("5")
# print("**", driver.nextGreatestLetter(["c", "f", "j"],"j"))
# print("-- 'c'")

# print("6")
# print("**", driver.nextGreatestLetter(["c", "f", "j"],"k"))
# print("-- 'c'")