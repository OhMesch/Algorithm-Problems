class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        first_len, second_len = len(text1)+1, len(text2)+1
        subproblem = [[0]*(first_len) for _ in range(second_len)]

        for j in range(1,second_len):
            for i in range(1,first_len):
                possibilities = [subproblem[j][i-1], subproblem[j-1][i]]
                if text1[i-1] == text2[j-1]:
                    possibilities.append(subproblem[j-1][i-1]+1)
                subproblem[j][i] = max(possibilities)

        [print(arr) for arr in subproblem]
        return subproblem[-1][-1]

driver = Solution()
print("1:")
print("--",driver.longestCommonSubsequence("abcde", "ace"))
print("**",3)

print("2:")
print("--",driver.longestCommonSubsequence("TEXT", "TEXT2"))
print("**",4)