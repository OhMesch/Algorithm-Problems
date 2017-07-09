# Problem: Given scores of N althletes
# Return their relative ranks and the people with the top 3 scores

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks = {}
        numsSorted = sorted(nums)
        numsSorted.reverse()
        output = []

        k = 0
        for i in range(len(numsSorted)):
            if i == 0:
                ranks[numsSorted[i]] = "Gold Medal"
            elif i == 1:
                ranks[numsSorted[i]] = "Silver Medal"
            elif i == 2:
                ranks[numsSorted[i]] = "Bronze Medal"
            else:
                ranks[numsSorted[i]] = i+1

        for elm in nums:
            output.append(str(ranks[elm]))

        return(output)

driver = Solution()

t1 = [5, 4, 3, 2, 1]
t2 = [1, 2, 3, 4, 5]
t3 = [15,4,18,19,20,25,99,80,76,10001,0,12]

print('\n')
print('atheletes:',t1, '\nranks:',driver.findRelativeRanks(t1),'\nExpected Answer:','["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]')
print('atheletes:',t2, '\nranks:',driver.findRelativeRanks(t2),'\nExpected Answer:','["5","4","Bronze Medal","Silver Medal","Gold Medal"]')
print('atheletes:',t3, '\nranks:',driver.findRelativeRanks(t3),'\nExpected Answer:',["9","11","8","7","6","5","Silver Medal","Bronze Medal","4","Gold Medal","12","10"])