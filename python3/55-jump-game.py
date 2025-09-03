class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        j = 0
        while True:
            if i == len(nums) - 1:
                return True
            if i == j and nums[i] == 0:
                return False
            j = max(j, i + nums[i])
            i += 1
