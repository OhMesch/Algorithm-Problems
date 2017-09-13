# Problem: Given a linked list and integer n
# Return: The linked list with the nth node deleted


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """ 
        fwd = head
        
        for i in range(n):
            fwd = fwd.next
            
        if fwd:
            curr=head
        else:
            return(head.next)
        
        while fwd.next:
            curr=curr.next
            fwd=fwd.next
        
        curr.next = curr.next.next
        
        return(head)