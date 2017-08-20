class Solution(object):
    def evalRPN(self, s):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for elm in s:
        	if elm in '+-*/':
        		if elm == "+":
        			stack.append(stack.pop()+stack.pop())
        		elif elm == "*":
        			stack.append(stack.pop()*stack.pop())
        		elif elm == "-":
        			temp = stack.pop()
        			stack.append(stack.pop()-temp)
        		else:
        			temp = stack.pop()
        			stack.append(int(float(stack.pop())/temp))
        	else:
        		stack.append(int(elm))

        return(stack.pop())

driver = Solution()

print("\n")

print("1")
print("**",driver.evalRPN(["2", "1", "+", "3", "*"]))
print("-- 9\n")

print("2")
print("**",driver.evalRPN(["4", "13", "5", "/", "+",]))
print("-- 6\n")

print("3")
print("**",driver.evalRPN(["4", "13", "5", "/", "+","2", "1", "+", "3", "*"]))
print("-- 9\n")

print("4")
print("**",driver.evalRPN(["18"]))
print("-- 18\n")

print("5")
print("**",driver.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print("-- 22\n")
