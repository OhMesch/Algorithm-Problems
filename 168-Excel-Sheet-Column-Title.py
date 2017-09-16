# Problem: Given a positive integer
# Return: Its corresponding column title as it would appear in Excel

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letters=[]
        key_dict={}
        
        for i in range(26):
            key_dict[i]=chr(i+65)
            
        while n != 0:
            n-=1
            letters.append(key_dict[n%26])
            n = n//26
            
        return(''.join(letters[::-1]))