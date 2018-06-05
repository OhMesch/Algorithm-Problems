# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        solSet = set()
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for word in words:
        	morseWord = ""
        	for char in word:
        		morseWord += MORSE[ord(char)-97]
        	solSet.add(morseWord)

        return(len(solSet))

driver = Solution()

print("1: ", driver.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]), " 2")