// 1431. Kids With the Greatest Number of Candies

// Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
// For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

#include <bits/stdc++.h>

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> sol;
        int max = 0;
        for (auto c : candies) {
            if (c > max) {max=c;}
        }
        for (int i = 0; i<candies.size(); i++) {
            sol.push_back(candies[i]+extraCandies >= max);
        }
        return sol;
    }
};