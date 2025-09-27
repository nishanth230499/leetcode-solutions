class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        mem = {}

        def choose(x1, x2):
            if abs(x1 - target) == abs(x2 - target):
                return x1 if x1 < x2 else x2
            if abs(x1 - target) < abs(x2 - target):
                return x1
            return x2

        def rec(i, cost):
            if i == len(toppingCosts):
                return cost
            
            if (i, cost) in mem:
                return mem[(i, cost)]

            res = rec(i + 1, cost)
            res = choose(res, rec(i + 1, cost + toppingCosts[i]))
            res = choose(res, rec(i + 1, cost + 2 * toppingCosts[i]))

            mem[(i, cost)] = res
            return res
        
        res = float("inf")
        for cost in baseCosts:
            res = choose(res, rec(0, cost))
        
        return res
            
