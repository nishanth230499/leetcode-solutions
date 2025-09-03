class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        max_sum = diff[0]
        max_sum_i = 0
        s = 0
        for i in range(len(diff)):
            s += diff[i]
            if s < max_sum:
                max_sum = s 
                max_sum_i = i
        return (max_sum_i + 1) % len(diff)