# Problem: Given a list of words
# Return: The words that can be spelled using only one row of the keyboard

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1=set('qwertyuiop')
        r2=set('asdfghjkl')
        r3=set('zxcvbnm')
        sol = []
        
        for word in words:
        	if any(word.count(s) > 0 for s in r1) and any(word.count(s) > 0 for s in r2):
        		continue
        	if any(word.count(s) > 0 for s in r2) and any(word.count(s) > 0 for s in r3):
        		continue
        	if any(word.count(s) > 0 for s in r3) and any(word.count(s) > 0 for s in r1):
        		continue
        	else:        
        		sol.append(word)
        return(sol)

driver = Solution()
t1 = ["Hello", "Alaska", "Dad", "Peace"]
t2 = ['a','q','z','az','qa','qz']

print('\n')
print('Array:',t1,'Program sol vs Expected sol:\n',driver.findWords(t1),'\n ["Alaska", "Dad"]\n')
print('Array:',t2,'Program sol vs Expected sol:\n',driver.findWords(t2),'\n ["a","z","q"]\n')