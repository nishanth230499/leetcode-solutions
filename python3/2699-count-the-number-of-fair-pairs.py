class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            l = bisect_left(nums, lower - nums[i], lo=i+1)
            r = bisect_right(nums, upper - nums[i], lo=i+1)
            ans += (r-l)
        return ans
        