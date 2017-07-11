# Problem: Given a string
# Return: THe reversed string

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = format(num,'b')
        sum =0
        for i in range(len(binary)):
        	if binary[::-1][i] == '0':
        		sum +=2**i
        return(sum)

driver = Solution()

t1 = 5
t2 = 25
print('\n')
print('Number',t1, '\nComplement:',driver.findComplement(t1),'\nExpected Answer:','2')
print('Number',t2, '\nComplement:',driver.findComplement(t2),'\nExpected Answer:','6')