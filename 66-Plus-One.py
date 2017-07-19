# Problem: Given an array representing an integer
# Return: One plus the given int

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ''
        for elm in digits:
            string += str(elm)
        string = str(int(string)+1)
        return(list(int(x) for x in list(string)))


            
driver = Solution()
t1 = [2,3,1,1,4]
t2 = [3,2,1,0,4]
t3 = [0]
t4 = [2,5,0,0]
t5 = [9]
t6 = [9,9]

print('\n')
print('Integer:',t1,'Program vs Expected sol:\n',driver.plusOne(t1),'\n [2,3,1,1,5]\n')
print('Integer:',t2,'Program vs Expected sol:\n',driver.plusOne(t2),'\n [3,2,1,0,5]\n')
print('Integer:',t3,'Program vs Expected sol:\n',driver.plusOne(t3),'\n [1]\n')
print('Integer:',t4,'Program vs Expected sol:\n',driver.plusOne(t4),'\n [2,5,0,1]\n')
print('Integer:',t5,'Program vs Expected sol:\n',driver.plusOne(t5),'\n [1,0]\n')
print('Integer:',t6,'Program vs Expected sol:\n',driver.plusOne(t6),'\n [1,0,0]\n')