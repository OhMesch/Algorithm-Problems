// 1433. Check If a String Can Break Another String
// Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa (in other words s2 can break s1).
// A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

class Solution {
public:
    bool checkIfCanBreak(string s1, string s2) {
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        
        int break_marker = 0;
        for(int i = 0; i<s1.size(); i++) {
            if (s1[i] > s2[i]) {
                if (break_marker == 0) {
                    break_marker = 1;
                } else if (break_marker == -1) {
                    return false;
                }
            }
            if (s1[i] < s2[i]) {
                if (break_marker == 0) {
                    break_marker = -1;
                } else if (break_marker == 1) {
                    return false;
                }
            }
        }
        return true;
    }
};