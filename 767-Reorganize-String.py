# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        d = {}
        l = len(S)
        sol_arr = []
        for char in S:
            d[char] = d.get(char,0) + 1
            if d[char] > (l+1)//2:
                return("")

        for k,v in sorted(d.items(), key = lambda x: (x[1],x[0])):
            sol_arr.extend(k*v)

        sol_arr[::2],sol_arr[1::2] = sol_arr[l//2:],sol_arr[:l//2]
        return("".join(sol_arr))

driver = Solution()

print('1')
print('**',driver.reorganizeString("aaggabba"))
print('-- ababagag\n')

print('2')
print('**',driver.reorganizeString("aab"))
print('-- aba\n')

print('3')
print('**',driver.reorganizeString("asdkfkljwieoqnfsadjksljdfkasndaiotnskdfnklsadfjsadfjnk"))
print('-- dfdfdfdfdfdfdjkjkjkjkjknknknsnsnslslslsisiaoaoaeaqataw\n')

print('4')
print('**',driver.reorganizeString("aaab"))
print('-- None\n')

print('5')
print('**',driver.reorganizeString("llllllllaaaaaaaaaaaaasssssssssswwwwwwwwwwww"))
print('-- awawawasasasasasasasasasaswlwlwlwlwlwlwlwlw\n')