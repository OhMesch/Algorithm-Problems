class Solution(object):
    def __init__(self):
        self.master = []
        self.key = {
                    '0': ' ',
                    '1': '*',
                    '2': 'acb',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz',
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return([])
        self.helper('',digits)
        return(self.master)

    def helper(self,curr,numbers):
        if len(numbers) == 1:
            for char in self.key[numbers]:
                self.master.append(curr+char)
        else:
            for char in self.key[numbers[0]]:
                self.helper(curr+char,numbers[1:])

driver = Solution()
print('\n')

print('1')
print('**',driver.letterCombinations('23'))
print('-- ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]\n')

print('2')
print('**',driver.letterCombinations(''))
print('-- \n')