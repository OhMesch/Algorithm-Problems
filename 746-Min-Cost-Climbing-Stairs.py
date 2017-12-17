# Problem:
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1. 

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 2:
            return(min(cost))
        for i in range(len(cost)-3,-1,-1):
            val = cost[i]
            cost[i] += min(cost[i+1],cost[i+2])
        return(min(cost[0],cost[1]))