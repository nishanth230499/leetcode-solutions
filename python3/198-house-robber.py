class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        soln = [None for _ in range(len(nums))]
        soln[0] = nums[0]
        soln[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            soln[i] = max(soln[i-1], nums[i]+soln[i-2])
        return soln[len(nums)-1]