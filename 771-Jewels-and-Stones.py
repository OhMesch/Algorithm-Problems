# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sol = 0
        jewels = set(J)

        for char in S:
            if char in jewels:
                sol += 1

        return(sol)

driver = Solution()

print('1')
print('**',driver.numJewelsInStones('aA','aAAbbbb'))
print('-- 3\n')

print('2')
print('**',driver.numJewelsInStones('z','ZZ'))
print('-- 0\n')