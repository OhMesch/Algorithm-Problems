# Problem: Given a series of directions:
# Up, down, right, left

# Return: Whether or not one ends in the original position

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        return(bool(moves.count("R")==moves.count("L") and moves.count("U")==moves.count("D")))

driver = Solution()

print('\n')

print('1')
print('**',driver.judgeCircle("UD"))
print("-- true\n")

print('2')
print('**',driver.judgeCircle("LL"))
print("-- false\n")