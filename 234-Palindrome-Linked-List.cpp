// Problem: Given a linked list
// Return: Whether or not it is a palindrome

#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(0) {}
};
 

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        std::vector <int> prev;
        ListNode* slow = head;
        ListNode* fast = head;
        int index = 0;
        bool even = false;
        int flip_val = 0;
        
        if(!head or (*head).next == NULL)
        {
            return(true);
        }
        
        while((*fast).next != NULL && (*((*fast).next)).next != NULL)
        {
            prev.push_back((*slow).val);
            fast = ((*(*fast).next).next);
            slow = (*slow).next;
            index++;
        }
        
        int mid = index;
        
        if(mid==0)
        {
            return(bool((*head).val==(*(*head).next).val));
        }
                           
        if((*fast).next != NULL)
        {
            prev.push_back((*slow).val);
            even = true;
        }
        
        index++;
        slow = (*slow).next;
        
        while(slow != NULL)
        {
            if(!even)
            {
                flip_val = prev[(2*mid)-index];
            }
            else
            {
                flip_val = prev[((2*mid)-index)+1];
            }
                        
            if(flip_val != (*slow).val)
            {
                return(false);
            }
            
            index++;
            slow = (*slow).next;
        }
        
        return(true);
    }
    
};