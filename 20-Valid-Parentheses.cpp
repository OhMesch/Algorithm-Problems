// Problem:
// Given a string of (, ), {, }, [, and ]
// Determing if the input string uses valid (),[], and {}

class Solution {
public:
    bool isValid(string s) {

        std::stack<char> open_para;
        int len = s.length();

        for(int i = 0; i < len; i++)
        {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[')
            {
                open_para.push(s[i]);
            }
            else
            {
                if(open_para.empty())
                {
                    return(false);
                }
                if(s[i] == ')' && open_para.top() != '(')
                {
                    return(false);
                }
                if(s[i] == '}' && open_para.top() != '{')
                {
                    return(false);
                }
                if(s[i] == ']' && open_para.top() != '[')
                {
                    return(false);
                }
                open_para.pop();
            }
        }
        if(open_para.empty())
        {
            return(true);
        }
        else
        {
            return(false);
        }
    }
};