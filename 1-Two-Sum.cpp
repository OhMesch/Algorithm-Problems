// Problem:
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> sol;
        std::unordered_map<int,int> dict;
        int i = 0;
        
        for(std::vector<int>::iterator iter = nums.begin(); iter != nums.end(); ++iter)
        {
            auto lookup = dict.find(*iter);
            if(lookup != dict.end())
            {
                return(std::vector<int> {lookup->second,i});
            }
            else
            {
                dict.insert(std::pair<int,int>(target-*iter,i));
            }
            i++;
        }
        return(sol);
    }
};