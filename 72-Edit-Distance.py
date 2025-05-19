class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        
        len_s1, len_s2 = len(word1)+1, len(word2)+1
        
        subproblem = [[0 for x in range(len_s2)] for y in range(len_s1)]
        for y in range(len_s1):
            subproblem[y][0] = y
        for x in range(len_s2):
            subproblem[0][x] = x
        for y in range(1,len_s1):
            for x in range(1,len_s2):
                subproblem[y][x] = min(1 + subproblem[y-1][x],\
                                       1 + subproblem[y][x-1],\
                                       1-(word1[y-1]==word2[x-1]) + subproblem[y-1][x-1])
                
        # [print(y) for y in subproblem]
        return subproblem[-1][-1]