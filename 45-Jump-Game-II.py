# Problem: Given an array of numbers representing max jump length from the current index
# Return: Return the minimium amount of jumps required to reach the end. 0 for impossible

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return(0)
        debug = False
        sol = len(nums)*[0]
        for i in range((len(nums)-1),-1,-1):
            if debug: print('index',i)
            if debug: print('number',nums[i])
            if i+nums[i] >= len(nums)-1:
                if debug: print('sol:',sol)
                sol[i] = 1
            elif any([x for x in sol[i:i+nums[i]+1] if x != 0]):
                if debug: print('sol',sol)
                sol[i] = min([x for x in sol[i:i+nums[i]+1] if x > 0]) + 1
        return(sol[0])

driver = Solution()
t1 = [2,3,1,1,4]
t2 = [3,2,1,0,4]
t3 = [0]
t4 = [2,5,0,0]
t5 = [1,2,4,1,2,1,4,3,1,0,2,1,2,3,1,1,2,1,2,3,0,1,3]

print('\n')
print('Jump Array:',t1,'Program vs Expected sol:\n',driver.canJump(t1),'\n 2\n')
print('Jump Array:',t2,'Program vs Expected sol:\n',driver.canJump(t2),'\n 0\n')
print('Jump Array:',t3,'Program vs Expected sol:\n',driver.canJump(t3),'\n 1\n')
print('Jump Array:',t4,'Program vs Expected sol:\n',driver.canJump(t4),'\n 2\n')
print('Jump Array:',t4,'Program vs Expected sol:\n',driver.canJump(t4),'\n 10\n')