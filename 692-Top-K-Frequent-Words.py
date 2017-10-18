class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        most_frequent = sorted(d.items(),key=lambda x: (-x[1],x[0]))
        return([x[0] for x in most_frequent[:k]])

driver = Solution()
print('\n')

print('0')
print('**',driver.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2))
print('-- ["i", "love"]')

print('1')
print('**',driver.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4))
print('-- ["the", "is", "sunny", "day"]')