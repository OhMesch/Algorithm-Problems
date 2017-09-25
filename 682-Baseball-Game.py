'''
Problem:
 You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

    Integer (one round's score): Directly represents the number of points you get in this round.
    "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
    "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
    "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.

Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds. 
'''


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        running_sum = 0
        valid_rounds = []
        for elm in ops:
            if elm == 'C':
                running_sum -= int(valid_rounds.pop())
            elif elm == 'D':
                double = 2*int(valid_rounds[-1])
                running_sum += double
                valid_rounds.append(str(double))
            elif elm == '+':
                comb = int(valid_rounds[-1])+int(valid_rounds[-2])
                running_sum += comb
                valid_rounds.append(str(comb))
            else:
                running_sum+=int(elm)
                valid_rounds.append(elm)
        return(running_sum)



driver = Solution()
print('\n')

print('**',driver.calPoints(["5","2","C","D","+"]))
print('-- 30\n')

print('**',driver.calPoints(["5","-2","4","C","D","9","+","+"]))
print('-- 27\n')