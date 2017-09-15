# Problem: Given a singularly linked list
# Return: The linked list reversed

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head:
            return([])
        
        node_list = [head]
        curr = head
        while curr.next:
            curr = curr.next
            node_list.append(curr)
            
        for node in (node_list[-2::-1]):
            curr.next = node
            curr = curr.next
        curr.next= None
        return(node_list[-1])