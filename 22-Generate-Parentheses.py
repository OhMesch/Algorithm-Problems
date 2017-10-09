#Problem: Given n pairs of parentheses
#Return: All combinations of well-formed parentheses

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.sol = []
        self.genPara(1,2*n-1,'(')
        return(self.sol)
        
    def genPara(self,open_para,space,para_str):
        if space-open_para > 0:
            self.genPara(open_para+1,space-1,para_str+'(')
        if open_para > 0 and space > 0:
            self.genPara(open_para-1,space-1,para_str+')')
        elif space == 0:
            self.sol.append(para_str)