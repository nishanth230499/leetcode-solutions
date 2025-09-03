class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = [{} for _ in range(len(nums))]
        def rec(i, t):
            if i == -1:
                return int(t == 0)
            if t not in mem[i]:
                mem[i][t] = rec(i-1, t + nums[i]) + rec(i-1, t - nums[i])
            return mem[i][t]
        
        return rec(len(nums) - 1, target)