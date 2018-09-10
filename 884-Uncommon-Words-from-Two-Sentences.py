class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        counter = dict()
        
        for wordA in A.split():
            counter[wordA] = counter.get(wordA,0) + 1

        for wordB in B.split():
            counter[wordB] = counter.get(wordB,0) + 1

        return([k for k,v in counter.items() if v == 1])

driver = Solution()
print("1:")
print("--",driver.uncommonFromSentences("this apple is sweet","this apple is sour"))
print("**",["sweet","sour"])

print("2:")
print("--",driver.uncommonFromSentences("apple apple","banana"))
print("**",["banana"])