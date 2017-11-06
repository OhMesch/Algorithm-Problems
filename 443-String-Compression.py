'''
Problem:
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.
'''

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        r = 0
        w = 0
        tracking = None
        counter = 0
        while(r < len(chars)):
            tracking = chars[r]
            while(r < len(chars) and chars[r] == tracking):
                counter += 1
                r += 1
            chars[w] = tracking
            w += 1
            if counter > 1:
                for char in str(counter):
                    chars[w] = char
                    w += 1
            counter = 0
        return(w)