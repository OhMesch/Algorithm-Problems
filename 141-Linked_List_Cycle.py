#Problem: Given a linked list, determine if it has a cycle in it. 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return(False)
        slow = head
        fast = head
        while True:
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return(False)
            slow = slow.next
            if fast is slow:
                return(True)