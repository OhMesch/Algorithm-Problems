# Problem: Given two sorted linked lists
# Return: A single merged sorted list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return([])
        
        head = ListNode(0)
        node = head
        
        while l1 and l2:
            if l1.val > l2.val:
                node.next = ListNode(l2.val)
                l2 = l2.next
            else:
                node.next = ListNode(l1.val)
                l1 = l1.next
            node = node.next
        if l1:
            node.next = l1
            
        elif l2:
            node.next = l2
        
        return(head.next)