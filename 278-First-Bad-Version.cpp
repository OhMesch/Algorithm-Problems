// 278. First Bad Version

// You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
// Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
// You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

#include <bits/stdc++.h>

class Solution {
public:
    int firstBadVersion(int n) {
        long long lower_bound = 1;
        long long upper_bound = n;
        
        long long mid_point;
        while(mid_point != n) {
            mid_point = (lower_bound+upper_bound) / 2;
            if (isBadVersion(mid_point)) {
                upper_bound = mid_point-1;
            }
            else {
                if (isBadVersion(++mid_point)) { break; }
                lower_bound = mid_point;
            }
        }
        return mid_point;
    }
};