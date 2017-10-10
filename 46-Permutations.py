class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.sol=[]
        self.genPerms([],nums)
        return(self.sol)

    def genPerms(self,curr,availible):
        if not availible:
            self.sol.append(curr)
            return
        for i in range(len(availible)):
            self.genPerms(curr+[availible[i]],availible[:i]+availible[i+1:])

driver = Solution()
print('\n')

print('1')
print('**',driver.permute([1,2,3]))
print('-- [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]\n')

print('2')
print('**',driver.permute([]))
print('-- [[]]\n')