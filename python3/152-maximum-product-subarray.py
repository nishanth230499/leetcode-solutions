class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_from_zero = 0
        suffix_from_zero = 0
        res = nums[0]
        for i in range(n):
            prefix_from_zero = (prefix_from_zero or 1) * nums[i]
            suffix_from_zero = (suffix_from_zero or 1) * nums[n - i - 1]
            res = max(res, max(prefix_from_zero, suffix_from_zero))
        return res