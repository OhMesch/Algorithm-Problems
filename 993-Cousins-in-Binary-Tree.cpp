// 993. Cousins in Binary Tree
// In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
// Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
// We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
// Return true if and only if the nodes corresponding to the values x and y are cousins.

#include <bits/stdc++.h>

class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
        if (root->val == x || root->val == y) {
            return false;
        }
        
        vector<TreeNode *> curr_depth {root};
        while (!curr_depth.empty()) {
            bool match_found_here = false;
            vector<TreeNode *> next_depth;
            for (auto node : curr_depth) {
                switch (this->countMatchingNodeChildValues(node, x, y)) {
                    case 1 :
                        if (match_found_here) {return true;}
                        else {match_found_here = true;}
                        break;
                    case 2 :
                        return false;
                        break;
                }
                
                if (node->left) {
                    next_depth.push_back(node->left);
                }
                if (node->right) {
                    next_depth.push_back(node->right);
                }
            }
            if (match_found_here) {return false;}
            curr_depth = next_depth;
        }
        return false;
    }
    
    int countMatchingNodeChildValues(TreeNode* node, int val_1, int val_2) {
        int count = 0;
        if(node->left) {
            count += static_cast<int>(node->left->val == val_1 || node->left->val == val_2);
        }
        if(node->right) {
            count += static_cast<int>(node->right->val == val_1 || node->right->val == val_2);
        }
        return count;
    }
};