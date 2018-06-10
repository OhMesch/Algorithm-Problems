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
        key = dict()
        mic = dict()
        sol = [0]*len(quiet)

        for i,j in richer:
            if i not in key:
                key[i] = Bank(j)
            else:
                key[i].addPeasent(j)
            if j not in richer:
                key[j] = Bank()

        for person,vol in enumerate(quiet):
            mic[vol] = person

        for person in range(len(quiet)):
            for vol in quiet:
                louderPerson = mic[vol]
                if key[louderPerson].xIsPeasent(person,key):
                    sol[person] = louderPerson
                    break

        return(sol)

class Bank:
    def __init__(self,peasent = None):
        self.richerThan = []
        if peasent:
            self.addPeasent(peasent)

    def addPeasent(self, peasent):
        self.richerThan.append(peasent)

    def xIsPeasent(self, x, key):
        if x in self.richerThan:
            return(True)
        else:
            for peasent in self.richerThan:
                if(key[peasent].xIsPeasent(x,key)):
                    return(True)
        return(False)





driver = Solution()
print("_1_")
print(driver.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],[3,2,5,4,6,1,7,0]))
print("[5, 5, 2, 5, 4, 5, 6, 7]\n")