class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums)-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l < r-1:
            m = (l+r)//2
            if nums[l] > nums[m]:
                r = m
            else:
                l = m
        return nums[r]