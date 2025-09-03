class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = -float("inf")
        cur_sum = 0
        for num in nums:
            cur_sum += num
            max_sub = max(max_sub, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sub