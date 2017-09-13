// Problem: Given a linked list and integer n
// Return: The linked list with the nth node deleted


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *fwd = head;
        ListNode *curr = head;
        
        for(int i = 0; i < n; i++)
        {
            fwd = fwd->next;
        }
        if(fwd == NULL)
        {
            return(head->next);
        }
        while(fwd->next != NULL)
        {
            curr = curr->next;
            fwd = fwd->next;
        }
        curr->next = curr->next->next;
        return(head);
    }
};