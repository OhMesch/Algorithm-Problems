// Problem: Given a non-empty string s
// Return: Whether or not it can be made a palidrone by deleting up to 1 character

class Solution {
public:
    bool validPalindrome(string s, bool deleted = false) {
        int l = 0;
        int r = s.length()-1;
        while(s[l] == s[r])
        {
            l += 1;
            r -= 1;
            if(l > r)
            {
                return(true);
            }
        }
        if(s[l] != s[r])
        {
            if(deleted)
            {
                return(false);
            }
            else
            {
                return(validPalindrome(s.substr(l,r-l),true) || validPalindrome(s.substr(l+1,r-l),true));
            }
        }
        
        string subString = s.substr(1,r-l);
        return(true);
    }
};