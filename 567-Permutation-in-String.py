class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1 and not s2:
            return(False)
        elif len(s1) > len(s2):
            return(False)
        elif not s1:
            return(True)

        key = self.make_count_arr(s1)

        slide_begin = 0
        slide_end = len(s1)

        window = self.make_count_arr(s2[slide_begin:slide_end])

        while slide_end < len(s2):
            if window == key:
                return(True)
            else:
                window[ord(s2[slide_begin])-97] -= 1
                window[ord(s2[slide_end])-97] += 1 
                slide_begin += 1
                slide_end += 1

        return(window == key)

    
    def make_count_arr(self,string):
        count_arr = 26*[0]
        for char in string:
            count_arr[ord(char)-97] += 1
        return(count_arr)


driver = Solution()
print('\n')

print('1')
print('**',driver.checkInclusion("ab","eidbaooo"))
print('-- True\n')

print('2')
print('**',driver.checkInclusion("ab","eidboaoo"))
print('-- False\n')

print('3')
print('**',driver.checkInclusion("","eidboaoo"))
print('-- True\n')

print('4')
print('**',driver.checkInclusion("",""))
print('-- False\n')

print('5')
print('**',driver.checkInclusion("a","bbbbbbbbbbbbbbbbbbba"))
print('-- True\n')