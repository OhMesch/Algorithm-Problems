# Problem:
# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

# For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

# Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.

# However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"]. 


class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        pair_d = {}
        if len(words1) != len(words2):
            return(False)
        for elm in pairs:
            pair_d[elm[0]] = (pair_d.get(elm[0],[]))+[elm[1]]
            pair_d[elm[1]] = (pair_d.get(elm[1],[]))+[elm[0]]
        for w1,w2 in zip(words1,words2):
            if w1 != w2 and (w2 not in pair_d.get(w1,[])):
                return(False)
        return(True)

# driver = Solution()
# print("\n")

# print('1')
# print('**',driver.areSentencesSimilar(["great"],["great"],[]))
# print('-- True\n')

# print('2')
# print('**',driver.areSentencesSimilar(["great","acting","skills"],["fine","drama","talent"],[["great","fine"],["drama","acting"],["skills","talent"]]))
# print('-- True\n')

# print('3')
# print('**',driver.areSentencesSimilar(["great","cat","skills"],["fine","drama","talent"],[["great","fine"],["drama","acting"],["skills","talent"]]))
# print('-- False\n')