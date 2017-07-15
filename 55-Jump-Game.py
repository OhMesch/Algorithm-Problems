# Problem: Given an array of numbers representing max jump length from the current index
# Return: True if the end of the array can be reached from the start or false if it cannot

class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		prev = [0]*len(nums)
		for i in range (len(nums)-1,-1,-1):
			if i + nums[i] >= len(nums) - 1:
				prev[i] = 1
			elif 1 in prev[i:i+nums[i]+1]:
				prev[i] = 1
		if prev[0]== 1:
			return(True)
		else:
			return(False)
driver = Solution()
t1 = [2,3,1,1,4]
t2 = [3,2,1,0,4]
t3 = [0]
t4 = [2,5,0,0]
print('\n')
print('Jump Array:',t1,'Program vs Expected sol:\n',driver.canJump(t1),'\n True\n')
print('Jump Array:',t2,'Program vs Expected sol:\n',driver.canJump(t2),'\n False\n')
print('Jump Array:',t3,'Program vs Expected sol:\n',driver.canJump(t3),'\n True\n')
print('Jump Array:',t4,'Program vs Expected sol:\n',driver.canJump(t4),'\n True\n')