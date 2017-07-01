class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()

        if amount == 0:
            return(1)

        if coins == []:
                return(0)
        
        combinations = [[0 for change in range(amount+1)] for coin in range(len(coins))]

        for row in range(len(coins)):
            for moneySum in range(coins[0],amount+1):
                #Establish terms for navigating through the 2D array
                currentCoin = coins[row]
                
                #Change can be delivered additionally in all new coin
                if (moneySum) % currentCoin == 0:
                    combinations[row][moneySum] += 1

                if row != 0:
                    #Always carry previous solutions
                    combinations[row][moneySum] += combinations[row-1][moneySum]

                    #Change requires previous combination of coins to suppliment new coin
                    remainder = moneySum - currentCoin
                    while remainder > 0:
                        combinations[row][moneySum] += combinations[row-1][remainder]
                        remainder -= currentCoin

        # Uncomment to visualize solutions       
        # testCounter = 0
        # print('   ',list(range(amount+1)))
        # for array in combinations:
        #     print([coins[testCounter]],array)
        #     testCounter += 1

        return(combinations[-1][-1])

driver = Solution()

print('\n')
print('\n Total: 3\n List: [2]\n',driver.change(3,[2]),'\n Answer: 0\n')
print('\n Total: 5\n List: [1,2,5]\n',driver.change(5,[1,2,5]),'\n Answer: 4\n')
print('\n Total: 4\n List: [1,2,3]\n',driver.change(4,[1,2,3]),'\n Answer: 4\n')
print('\n Total: 10\n List: [2,5,3,6]\n',driver.change(10,[2,5,3,6]),'\n Answer: 5\n')
print('\n Total: 5000\n List: [11,24,37,50,63,76,89,102]\n',driver.change(5000,[11,24,37,50,63,76,89,102]),'\n Answer: 992951208\n')