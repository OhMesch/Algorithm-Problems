//Problem: Given a binary tree
//Return: Find the sum of all left leaves

#include <iostream>

 // Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(0), right(0) {}
 };
 
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if(!root)
        {
            return 0;
        }

        int total = 0;

        if((*root).left)
        {
            if((*this).children((*root).left))
            {
                total += (*this).sumOfLeftLeaves((*root).left);
            }
            else
            {
                total += (*((*root).left)).val;
            }
        }

        if((*root).right)
        {
            total += (*this).sumOfLeftLeaves((*root).right);
        }
    }

    bool children(TreeNode* node)
    {
        return(bool((*node).left) or bool((*node).right));
    }

};



int main()
{
    std::cout << "Test";
    return 0;
}