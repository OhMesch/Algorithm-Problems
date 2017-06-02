class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		
		l1Array = []
		l2Array = []

		while(l1.next != None):
			l1Array.insert(0,l1.val)
			l1 = l1.next
		l1Array.insert(0,l1.val)

		while(l2.next != None):
			l2Array.insert(0,l2.val)
			l2 = l2.next
		l2Array.insert(0,l2.val)

		l1Array = ''.join(str(elm) for elm in l1Array)
		l2Array = ''.join(str(elm) for elm in l2Array)
		reverseAns = int(l1Array) + int(l2Array)

		Ans = []

		for elm in str(reverseAns):
			Ans.insert(0,elm)
		
		if len(Ans) == 1:
			listAnsStart = ListNode(Ans[0])

		else:

			listAnsStart = ListNode(Ans[0])
			listAnsNext = ListNode(Ans[1])
			listAnsStart.next = listAnsNext

			for index in range(2,len(Ans)):
				listAnsNext.next = ListNode(Ans[index])
				listAnsNext = listAnsNext.next

		return(listAnsStart)

# linkedList = ListNode(2)
# linkedList.next = ListNode(4)
# linkedList.next.next = ListNode(3)

# linkedList2 = ListNode(5)
# linkedList2.next = ListNode(6)
# linkedList2.next.next = ListNode(4)

# driver = Solution()
# print(driver.addTwoNumbers(linkedList,linkedList2))

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
# 	def addTwoNumbers(self, l1, l2):
# 		"""
# 		:type l1: ListNode
# 		:type l2: ListNode
# 		:rtype: ListNode
# 		"""
		
# string = '(2 -> 4 -> 3) + (5 -> 6 -> 4)'
# number = string.split('+')
# l1 = number[0]
# l2 = number[1]
# l1 = l1.replace(' ', '')
# l2 = l2.replace(' ', '')
# l1 = l1.replace('->', '')
# l2 = l2.replace('->', '')
# l1 = l1[1:-1]
# l2 = l2[1:-1]

# l1Actual =  []
# l2Actual =  []
# for digit in l1:
# 	l1Actual.insert(0,digit)
# for digit in l2:
# 	l2Actual.insert(0,digit)

# l1Actual =''.join(l1Actual)
# l2Actual =''.join(l2Actual)

# ansActual = int(l1Actual) + int(l2Actual)
# textAnsAct = str(ansActual)
# textAns = []

# for digit in textAnsAct:
# 	textAns.insert(0,digit)

# output = []
# output = ' -> '.join(textAns)

# print(output)

