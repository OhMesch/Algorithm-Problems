# In a group of N people (labelled 0, 1, 2, ..., N-1), each person has different amounts of money, and different levels of quietness.

# For convenience, we'll call the person with label x, simply "person x".

# We'll say that richer[i] = [x, y] if person x definitely has more money than person y.  Note that richer may only be a subset of valid observations.

# Also, we'll say quiet[x] = q if person x has quietness q.

# Now, return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]), among all people who definitely have equal to or more money than person x.

# 1 <= quiet.length = N <= 500
# 0 <= quiet[i] < N, all quiet[i] are different.
# 0 <= richer.length <= N * (N-1) / 2
# 0 <= richer[i][j] < N
# richer[i][0] != richer[i][1]
# richer[i]'s are all different.
# The observations in richer are all logically consistent.


class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        numberPeople = len(quiet)
        self.personalBanks = [[] for x in range(numberPeople)]
        self.quiet = quiet
        self.richer = richer
        self.loudestRichest = [None]*numberPeople
        sol = [0]*numberPeople

        self.createBanks()

        for i in range(numberPeople):
            sol[i] = self.getLoudestRichest(i)

        return(sol)

    def createBanks(self):
        for rich, poor in self.richer:
            self.personalBanks[poor].append(rich)
        print(self.personalBanks)

    def getLoudestRichest(self, person):
        if self.loudestRichest[person] == None:
            self.loudestRichest[person] = person
            self.updateLoudestRichest(person)
        return(self.loudestRichest[person])

    def updateLoudestRichest(self, person):
        queue = self.personalBanks[person]
        while queue:
            newQ = []
            for richer in queue:
                self.checkNewLoudestRichest(person,richer)
                newQ.extend(self.personalBanks[richer])
            queue = newQ


    def checkNewLoudestRichest(self, person, richer):
        currLoudest = self.loudestRichest[person]
        currChill = self.quiet[currLoudest]
        challengerLoudest = self.getLoudestRichest(richer)
        challengerChill = self.quiet[challengerLoudest]
        self.loudestRichest[person] = min((currLoudest, currChill), (challengerLoudest, challengerChill), key=lambda x: x[1])[0]

driver = Solution()
print("_1_")
print(driver.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],[3,2,5,4,6,1,7,0]))
print("[5, 5, 2, 5, 4, 5, 6, 7]\n")

print("_2_")
print(driver.loudAndRich([],[0,1]))
print("[0, 1]\n")

print("_3_")
print(driver.loudAndRich([[0,1]],[0,1]))
print("[0, 0]\n")