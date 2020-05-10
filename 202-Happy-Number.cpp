#include <iostream>
#include <cmath>
#include <unordered_set>

// Problem: Given an integer
// Return: Whether or not the integer is a happy number

/*
A happy number is a number defined by the following process: 
Starting with any positive integer, 
replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
*/

class Solution {
private:
    std::unordered_set<int> seen_;
public:
    bool isHappy(int n) {
        seen_.insert(n);

        int happiness = this->sumOfDigitsSquared(n);
        std::cout << happiness << std::endl;
        if (happiness == 1) {
            return true;
        }
        else if (seen_.find(happiness) != seen_.end()) {
            return false;
        }
        else {
            return this->isHappy(happiness);
        }
    }

    int sumOfDigitsSquared(int num) {
        int cum_sum = 0;
        while(num > 0) {
            cum_sum += std::pow((double) (num % 10), 2);
            num /= 10;
        }
        return cum_sum;
    }
};