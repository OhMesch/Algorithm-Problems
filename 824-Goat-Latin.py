# A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

# The rules of Goat Latin are as follows:

#     If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
#     For example, the word 'apple' becomes 'applema'.
     
#     If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
#     For example, the word "goat" becomes "oatgma".
     
#     Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#     For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

# Return the final sentence representing the conversion from S to Goat Latin.

class Solution:
    def __init__(self):
        self.sol = ""
        self.vowels = {"A","E","I","O","U","a","e","i","o","u"}
        self.a = ""
        self.newWord = True
        self.index = 0
        self.input = None
        self.inLength = 0

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        self.input = S
        self.inLength = len(S)

        while self.index < self.inLength:
            self.readToken(S[self.index])

        self.addToSol(self.a)
        print("")
        print(self.sol)
        return(self.sol)

    def readToken(self,token):
        if token == " ":
            self.tokenIsSpace(token)
        elif token not in self.vowels:
            self.tokenIsConst(token)
        else:
            self.tokenIsVowel(token)

    def tokenIsSpace(self,token):
        self.newWord = True
        while self.index < self.inLength and self.input[self.index] == " ":
            self.index += 1

    def tokenIsConst(self,token):
        self.checkNewWord()
        wordWithoutFirst = ""
        charToAppend = token + "ma"

        self.index += 1
        while self.index < self.inLength and self.input[self.index] != " ":
            wordWithoutFirst += self.input[self.index]
            self.index += 1

        self.addToSol(wordWithoutFirst+charToAppend)

    def tokenIsVowel(self,token):
        self.checkNewWord()
        word = ""
        charToAppend = "ma"

        while self.index < self.inLength and self.input[self.index] != " ":
            word += self.input[self.index]
            self.index += 1

        self.addToSol(word+charToAppend)


    def checkNewWord(self):
        if self.newWord:
            self.newWord = False
            self.addToSol(self.a)
            self.addToSol(" ")
            self.a += "a"

    def addToSol(self, addition):
        if addition == " " and self.sol:
            self.sol += " "
        elif addition != " ":
            self.sol += addition

# unitTester = Solution()
# assert(unitTester.toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
# assert(unitTester.toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
# assert(unitTester.toGoatLatin("   This is a space    test ") == "hisTmaa ismaaa amaaaa pacesmaaaaa esttmaaaaaa")