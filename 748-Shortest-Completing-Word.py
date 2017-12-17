# Problem:
# Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

# Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

# It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

# The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does. 

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        smallest = None
        alpha = set("abcdefghijklmnopqrstuvwxyz")
        nums = set("1234567890 ")
       	letters = [x.lower() for x in licensePlate if x not in nums]
       	print("Printing letters:",letters)
       	for word in words:
       		if smallest == None or len(word) < len(smallest):
       			if set(letters).issubset(set(word)):
       				potential = True
       				seen = set()
       				print("Trying:", word)
       				for letter in word:
       					if letter not in seen:
       						seen.add(letter)
       						if word.count(letter) < letters.count(letter):
       							potential = False
       				if potential:
       					smallest = word
       					potential = False
       	return(smallest)

        
driver = Solution()
print("\n")

print("1")
print("**", driver.shortestCompletingWord("1s3 PSt",["step", "steps", "stripe", "stepple"]))
print('-- steps\n')

print("2")
print("**", driver.shortestCompletingWord("1s3 456",["looks", "pest", "stew", "show"]))
print('-- pest\n')

print("3")
print("**", driver.shortestCompletingWord("tR28607",["present","fall","make","change","everything","performance","owner","beat","name","serve"]))
print('-- present\n')
