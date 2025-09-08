class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        res = 0
        start = 0
        end = 1
        prev_diff = nums[end] - nums[start]

        while True:
            if end + 1 < len(nums) and nums[end + 1] - nums[end] == prev_diff:
                end += 1
            else:
                n = end - start + 1
                res += (n-2) * (n-1) // 2
                start = end
                end += 1
                if end == len(nums):
                    break
                prev_diff = nums[end] - nums[start]
        
        return res


