// 1432. Max Difference You Can Get From Changing an Integer
// You are given an integer num. You will apply the following steps exactly two times:
//     Pick a digit x (0 <= x <= 9).
//     Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
//     Replace all the occurrences of x in the decimal representation of num by y.
//     The new integer cannot have any leading zeros, also the new integer cannot be 0.
// Let a and b be the results of applying the operations to num the first and second times, respectively.
// Return the max difference between a and b.

#include <bits/stdc++.h>

class Solution {
public:
    int maxDiff(int num) {
        return maxNumSingleRep(to_string(num)) - minNumSingleRep(to_string(num));
    }
    
    int maxNumSingleRep(string num) {
        int max = 0;
        bool seen[10] = {0};
        for(int i=0; i<num.size(); i++) {
            if (!seen[num[i]-'0']) {
                seen[num[i]-'0'] = true;
                string test_num = substituteString(num, num[i], '9');
                if (stoi(test_num) > max) {max = stoi(test_num);}
            }
        }
        return max;
    }
        
    int minNumSingleRep(string num) {
        int min = stoi(num);
        bool seen[10] = {0};
        for(int i=0; i<num.size(); i++) {
            string test_num;
            if (!seen[num[i]-'0']) {
                seen[num[i]-'0'] = true;
                if (i != 0) {
                    test_num = substituteString(num, num[i], '0');
                } else if (i == 0 || stoi(test_num) == 0) {
                    test_num.clear();
                    test_num = substituteString(num, num[i], '1');
                }
                if (stoi(test_num) < min) {min = stoi(test_num);}
            }
        }
        return min;
    }
    
    string substituteString(string str, char char_to_replace, char replacement) {
        string substitution;
        for (auto c : str) {
            if (c == char_to_replace) {
                substitution += replacement;
            } else {
                substitution += c;
            }
        }
        return substitution;
    }
};