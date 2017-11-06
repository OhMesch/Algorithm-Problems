'''
Problem:
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
'''

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        elif len(bits) == 0:
            return False
        if bits[0] == 1:
            return(self.isOneBitCharacter(bits[2:]))
        else:
            return(self.isOneBitCharacter(bits[1:]))