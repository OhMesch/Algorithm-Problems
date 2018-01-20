 // Problem:
 // Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

 // (Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.) 

 // Note:

 //     L, R will be integers L <= R in the range [1, 10^6].
 //     R - L will be at most 10000.

class Solution {
public:
    int countPrimeSetBits(int L, int R) {
        int sol = 0;
        std::set<int> primes = {2,3,5,7,11,13,17,19};

        for(int i = L; i<= R; i++)
        {
        	if(primes.find(__builtin_popcount(i)) != primes.end())
        	{
        		sol++;
        	}
        }
        return(sol);
    }
};