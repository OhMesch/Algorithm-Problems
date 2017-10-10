#Problem: Given a collection of numbers that might contain duplicates
#Return: All possible unique permutations. 

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.sol=[]
        self.genPerms([],sorted(nums))
        return(self.sol)

    def genPerms(self,curr,availible):
        if not availible:
            self.sol.append(curr)
        prev = None
        for i in range(len(availible)):
            if availible[i]==prev:
                continue
            self.genPerms(curr+[availible[i]],availible[:i]+availible[i+1:])
            prev=availible[i]

driver = Solution()
print('\n')

print('1')
print('**',driver.permuteUnique([1,2,3]))
print('-- [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]\n')

print('2')
print('**',driver.permuteUnique([]))
print('-- [[]]\n')

print('3')
print('**',driver.permuteUnique([1,1,2]))
print('-- [[1, 1, 2], [1, 2, 1], [2, 1, 1]]\n')

print('4')
print('**',driver.permuteUnique([3,3,0,0,2,3,2]))
print('-- too long\n')