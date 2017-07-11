class Solution(object):
	def arrayPairSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		pairs = list(zip(sorted(nums)[::2],sorted(nums)[1::2]))
		return(sum(list(map(lambda x:min(x),pairs))))

driver = Solution()

t1 = [1,4,3,2]
t2 = [17,18,34,59,2,70,54,76,100,122,1547,162]

print('\n')
print('Array:',t1,'\nProgram vs Expected Answer:\n',driver.arrayPairSum(t1),'\n 4\n')
print('Array:',t2,'\nProgram vs Expected Answer:\n',driver.arrayPairSum(t2),'\n 406\n')