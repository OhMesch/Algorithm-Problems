'''
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  Here, we have groups, of adjacent letters that are all the same character, and adjacent characters to the group are different.  A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the first example, and "i" would be extended in the second example.  As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that string.

For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.  Formally, we are allowed to repeatedly choose a group (as defined above) of characters c, and add some number of the same character c to it so that the length of the group is 3 or more.  Note that we cannot extend a group of size one like "h" to a group of size two like "hh" - all extensions must leave the group extended - ie., at least 3 characters long.

Given a list of query words, return the number of words that are stretchy. 
'''

'''
    0 <= len(S) <= 100.
    0 <= len(words) <= 100.
    0 <= len(words[i]) <= 100.
    S and all words in words consist only of lowercase letters
'''

class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            if self.isExpressiveWord(word,S):
                count += 1
        return(count)

    def isExpressiveWord(self, word, S):
        totalChars = len(S)
        if len(word) > totalChars:
            return(False)
        
        sIdx = 0
        wIdx = 0

        while sIdx < totalChars:
            if wIdx >= len(word):
                return(False)
            sChar = S[sIdx]
            wChar = word[wIdx]
            sLen = 0
            wLen = 0

            while sIdx < totalChars and sChar == S[sIdx]:
                sLen += 1
                sIdx += 1
            while wIdx < len(word) and wChar == word[wIdx]:
                wLen += 1
                wIdx += 1

            if sChar != wChar:
                return(False)

            if sLen < wLen:
                return(False)
            elif sLen != wLen and sLen < 3: 
                return(False)

        return(True)

driver = Solution()
print("1:",driver.expressiveWords("heeellooo", ["hello", "hi", "helo"])," 1")
print("2:",driver.expressiveWords("abcd", ['abc'])," 0")