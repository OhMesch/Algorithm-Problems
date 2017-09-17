// Problem: Given a positive integer
// Return: Its corresponding column title as it would appear in Excel

class Solution {
public:
    string convertToTitle(int n) {
        char letters[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
        string answer;
        while(n != 0)
        {
            n--;
            answer = letters[n%26] + answer;
            n = n/26;
        }
        return(answer);
    }
};
