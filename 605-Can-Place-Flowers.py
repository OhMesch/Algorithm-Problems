'''
Problem:
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        can_plant = 0
        if len(flowerbed) < 2:
            if n == 0:
                return(True)
            elif n == 1:
                return(not flowerbed[0])
            else:
                return(False)
        if flowerbed[0] == flowerbed[1] == 0:
            can_plant += 1
            flowerbed[0] = 1
        if flowerbed[-1] == flowerbed[-2] == 0:
            can_plant += 1
            flowerbed[-1] = 1
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                can_plant+=1
        return(can_plant >= n)