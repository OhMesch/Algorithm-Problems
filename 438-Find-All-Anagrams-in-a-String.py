# Problem:
# Given a singly linked list

# Return: 
# All odd nodes together followed by the even nodes.
# Odd nodes refer to placement in list, not value. The first node is odd, second even, ect.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return([])
        
        count = 2
        sol = ListNode(head.val)
        solStart = sol
        head = head.next
        first = True
        
        while head:
            if count % 2 == 0:
                if first:
                    even = ListNode(head.val)
                    evenStart = even
                    first = False
                else:
                    even.next = ListNode(head.val)
                    even = even.next
            else:
                sol.next = ListNode(head.val)
                sol = sol.next
            head = head.next
            count +=1
        if not first:
            sol.next = evenStart
        return(solStart)