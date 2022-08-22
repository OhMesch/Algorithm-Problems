#include <iostream>
#include <map>
#include <vector>

// Problem:
// Given an array of strings
// Return all anagrams group together

// Notes
// All inputs will be in lowercase.
// The order of your output does not matter.


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> anagrams;
        for (string word : strs)
        {
            string sorted_word = word;
            sort(sorted_word);

            if(map.find(sorted_word) != map.end())
            {
                map[sorted_word].
            }
        }
    }
};