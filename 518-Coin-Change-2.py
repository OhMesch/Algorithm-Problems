class Money(object):
    def coin(self, total, coinList):
        """
        :type total: int
        :type coinList: List
        :rtype: int
        """

        coinList.sort()
        
        combinations = [[0 for change in range(total)] for coin in range(len(coinList))]

        for row in range(len(coinList)):
            for changeIndex in range(total):

                #Establish easy terms for navigating through the 2D array
                #currentElm = combinations[row][changeIndex]
                aboveElm = combinations[row-1][changeIndex]
                currentCoin = coinList[row]
                moneySum = changeIndex+1
                
                #Establish a base case
                if row == 0:
                    if (moneySum) % coinList[0] == 0:
                        combinations[0][changeIndex] = 1
                else:
                    #Carry prior if new coin is too big for total
                    if currentCoin > moneySum: 
                        combinations[row][changeIndex] = aboveElm
                  
                    #New coin is same size as change to be tendered
                    elif currentCoin == moneySum: #This one might be eztranious
                        combinations[row][changeIndex] = aboveElm + 1

                    #Change to be tendered can be given in all new coins
                    if (moneySum)%currentCoin == 0:   
                        combinations[row][changeIndex] = aboveElm + 1

                    #New coin can go into total but needs other coins to suppliment
                    # remainder = total
                    # while remainder > currentCoin:
                    #     remainder -= coinList[row]
                    #     if combinations[row-1][remainder-1] != 0:
                    #         combinations[row][changeIndex] += combinations[row-1][remainder-1]
                    #         break




        testCounter = 0
        print('   ',list(range(1,total+1)))
        for array in combinations:
            print([coinList[testCounter]],array)
            testCounter += 1

        return((max(list(map(max,combinations)))))

        

driver = Money()

print('\n')
print('\n Total: 4\n List: [1,2,3]\n',driver.coin(4,[1,2,3]),'\n Answer: 4\n')
print('\n Total: 10\n List: [2,5,3,6]\n',driver.coin(10,[2,5,3,6]),'\n Answer: 5\n')