# Problem: Given a linked list and a value to remove
# Return: The linked list with all nodes of value val removed

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if head:
            start = head
        else:
            return([])
        while head:
            if head.val != val:
                prev = head
            else:
                prev.next = head.next
            head = head.next
        return(start)