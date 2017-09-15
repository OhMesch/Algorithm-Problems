// Problem: Given a singularly linked list
// Return: The linked list reversed

// Definition for singly-linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};
 

class Solution {
public:
    ListNode* reverseList(ListNode* head, ListNode* history = NULL) 
    {
        if (head == NULL)
        {
            return(history);
        }
        ListNode* next_head = head->next;
        head->next = history;
        return(reverseList(next_head,head));
    }
};