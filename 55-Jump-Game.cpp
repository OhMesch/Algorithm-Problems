// Problem:
// Given an array of non-negative integers, you are initially positioned at the first index of the array.
// Each element in the array represents your maximum jump length at that position.
// Determine if you are able to reach the last index. 

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int closest_winning_index = nums.size();
        for(int i = nums.size()-1; i > -1; i--)
        {
            if(i + nums[i] >= closest_winning_index || i +nums[i] >= nums.size()-1)
            {
                closest_winning_index = i;
            }
        }
        return(bool(!closest_winning_index));
    }
};