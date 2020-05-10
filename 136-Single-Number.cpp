#include <iostream>
#include <vector>

// Problem:
// Given a non-empty array of integers, every element appears twice except for one. 
// Find that single one.

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        int single_number = nums[0];
        for(auto num_iter = nums.begin()+1; num_iter != nums.end(); num_iter++)
        {
            single_number ^= *num_iter;
        }
        return single_number;
    }
};