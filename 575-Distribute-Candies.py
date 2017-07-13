# Problem: Given an even number of candies of seeral types and a brother and sister
# Return: The maximium number of unique candies the sister can get if the candy is divided evenly

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candiesEach = len(candies)/2
        uniqueCandies = set(candies)
        return(int(min(candiesEach,len(uniqueCandies))))

driver = Solution()

t1 = [1,1,2,2,3,3]
t2 = [1,1,2,3]

print('Array:',t1,'Program vs Expected sol:\n',driver.distributeCandies(t1),'\n 3\n')
print('Array:',t2,'Program vs Expected sol:\n',driver.distributeCandies(t2),'\n 2\n')