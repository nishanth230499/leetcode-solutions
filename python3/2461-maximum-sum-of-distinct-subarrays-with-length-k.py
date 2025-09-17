class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        vis = set()
        res = 0
        tot = 0

        while right < len(nums):
            while nums[right] in vis or right - left + 1 > k:
                vis.remove(nums[left])
                tot -= nums[left]
                left += 1
            
            vis.add(nums[right])
            tot += nums[right]

            if right - left + 1 == k:
                res = max(res, tot)

            right += 1
        
        return res
