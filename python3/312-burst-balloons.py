class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        mem = [[None for _ in range(len(nums))] for _ in range(len(nums))]

        def get_num(i):
            if 0 <= i < len(nums):
                return nums[i]
            return 1

        def rec(s, e):
            if s > e:
                return 0
            if mem[s][e] != None:
                return mem[s][e]
            res = 0
            for i in range(s, e + 1):
                coins = get_num(s-1) * nums[i] * get_num(e+1)
                coins += rec(s, i-1)
                coins += rec(i+1, e)
                res = max(res, coins)
            mem[s][e] = res
            return res
        
        return rec(0, len(nums) - 1)