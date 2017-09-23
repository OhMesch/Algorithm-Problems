// Problem: Given the number of starting stones in a game of nim
// Return: Will you win if you play properly and go first

// Nim: There is a heap of stones on the table.
// You take turns to remove 1 to 3 stones. 
// The one who removes the last stone will be the winner.

class Solution {
public:
    bool canWinNim(int n) {
        return(n%4);
    }
};