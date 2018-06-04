# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        bannedList = set(banned)
        wordCounter = dict()
        maxHit = 0
        maxWord = ""

        cleanParagraph = self.cleanParagraph(paragraph)

        for word in [x for x in cleanParagraph.split() if x not in bannedList]:
        	wordCounter[word] = wordCounter.get(word, 0) + 1
        	if wordCounter[word] > maxHit:
        		maxHit = wordCounter[word]
        		maxWord = word

        return(maxWord)

    def cleanParagraph(self,dirtyParagraph):
    	punctuation = [".",",","?","!","'",";"]
    	lowerPara = dirtyParagraph.lower()
    	cleanPara = "".join([x for x in lowerPara if x not in punctuation])
    	return(cleanPara)

driver = Solution()

print("1: ", driver.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]), " ball")