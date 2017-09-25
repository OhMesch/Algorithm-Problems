/*
Problem:
 You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

    Integer (one round's score): Directly represents the number of points you get in this round.
    "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
    "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
    "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.

Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds. 
*/


class Solution {
public:
    int calPoints(vector<string>& ops) {
        int running_sum = 0;
        std::stack<int> round;
        for(int i = 0; i < ops.size(); i++)
        {
            if(ops[i]=="C")
            {
                running_sum -= round.top();
                round.pop();
            }
            else if(ops[i]=="D")
            {
                int double_val = 2*round.top();
                running_sum += double_val;
                round.push(double_val);
            }
            else if(ops[i]=="+")
            {
                int top_val = round.top();
                round.pop();
                int comb = top_val + round.top();
                round.push(top_val);
                running_sum += comb;
                round.push(comb);
            }
            else
            {
                running_sum += stoi(ops[i]);
                round.push(stoi(ops[i]));
            }
        }
        return(running_sum);
    }
};