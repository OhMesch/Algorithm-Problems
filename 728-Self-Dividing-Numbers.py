class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def selfDividing(num):
        	for char in str(num):
        		if char == '0':
        			return(False)
        		elif num % int(char) != 0:
        			return(False)
        	return(True)

        return([x for x in range(left,right+1) if selfDividing(x)])