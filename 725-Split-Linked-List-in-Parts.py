class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node = root
        count = 0
        sol = []
        while node:
            node = node.next
            count += 1
        less_length = (count // k)
        num_greater = (count % k)
            
        curr = root
        while curr:
            if num_greater:
                size = less_length+1
                num_greater -= 1
            else:
                size = less_length
                
            clone = ListNode(curr.val)
            sol.append(clone)
            # if size <= 1:
                # curr = curr.next
            for i in range(size-1):
                curr = curr.next
                clone.next = ListNode(curr.val)
                clone = clone.next
            curr = curr.next

        if len(sol) < k:
            sol += [[] for x in range(k-len(sol))]

        return(sol)