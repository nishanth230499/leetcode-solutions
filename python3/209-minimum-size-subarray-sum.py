class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        res = float("inf")

        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                res = min(res, right - left + 1)
                if left == right:
                    break
                sum -= nums[left]
                left += 1
        
        return res if res != float("inf") else 0
