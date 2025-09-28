class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        self.res = 0
        def rec(i, nums_or):
            if i == len(nums):
                if nums_or == max_or:
                    self.res += 1
            else:
                rec(i + 1, nums_or)
                rec(i + 1, nums_or | nums[i])
        
        rec(0, 0)
        return self.res