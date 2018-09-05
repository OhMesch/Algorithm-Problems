# You are given an array A of strings.

# Two strings S and T are special-equivalent if after any number of moves, S == T.

# A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

# Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.

# Return the number of groups of special-equivalent strings from A.

# 1 <= A.length <= 1000
# 1 <= A[i].length <= 20
# All A[i] have the same length.
# All A[i] consist of only lowercase letters.

class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return(len({self.genKey(s) for s in A}))

    def genKey(self, string):
        key = [0]*52
        for i in range(len(string)):
            char = string[i]
            key[ord(char)-97+26*(i%2)] += 1
        return(tuple(key))



driver = Solution()

print("0:")
print("**",driver.numSpecialEquivGroups(["a","b","c","a","c","c"]))
print("-- 3")


print("1:")
print("**",driver.numSpecialEquivGroups(["aa","bb","ab","ba"]))
print("-- 4")

print("2:")
print("**",driver.numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))
print("-- 3")

print("3:")
print("**",driver.numSpecialEquivGroups(["abcd","cdab","adcb","cbad"]))
print("-- 1")