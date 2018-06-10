# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to closest person.

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        self.max = 0
        self.distance = [20001]*len(seats)

        self.checkForward(seats)
        self.checkBackwards(seats)

        return(self.max)

    def checkForward(self, seats):
        i = 0
        while seats[i] == 0:
            i+=1
        lastPerson = i

        while i < len(seats):
            if seats[i] == 1:
                lastPerson = i
            self.distance[i] = i-lastPerson
            i+=1



    def checkBackwards(self, seats):
        i = len(seats)-1
        while seats[i] == 0:
            self.checkIndexForMax(i)
            i-=1

        lastPerson = i

        while i >= 0:
            if seats[i] == 1:
                lastPerson = i
            self.distance[i] = min(self.distance[i],lastPerson-i)
            self.checkIndexForMax(i)
            i-=1


    def checkIndexForMax(self, i):
        self.max = max(self.max,self.distance[i])


driver = Solution()
print("_1_")
print(driver.maxDistToClosest([1,0,0,0,1,0,1]))
print("2\n")

print("_2_")
print(driver.maxDistToClosest([1,0,0,0]))
print("3\n")

print("_3_")
print(driver.maxDistToClosest([0,0,0,1]))
print("3\n")