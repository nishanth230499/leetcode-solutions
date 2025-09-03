class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        mem = [None for _ in range(len(cost))]

        def rec(i):
            if i == 0 or i == 1:
                return cost[i]
            if mem[i] != None:
                return mem[i]
            
            mem[i] = min(rec(i-1), rec(i-2)) + cost[i]
            return mem[i]
        
        return min(rec(len(cost)-1), rec(len(cost)-2))
        