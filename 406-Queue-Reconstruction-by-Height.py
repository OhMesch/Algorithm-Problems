'''
Problem:
Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.
'''


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sol=[]
        ordered_people = sorted(people,key=lambda x: (-x[0],x[1]))
        for i in range(len(ordered_people)):
            sol.insert(ordered_people[i][1],ordered_people[i])
        return(sol)


driver = Solution()
print('\n')

print('1')
print('**',driver.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
print('-- [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]\n')

print('2')
print('**',driver.reconstructQueue([[6,1],[10,0],[4,5],[7,0],[8,0],[3,1],[4,1],[6,4]]))
print('-- [[7, 0], [3, 1], [4, 1], [6, 1], [8, 0], [10, 0], [4, 5], [6, 4]]\n')