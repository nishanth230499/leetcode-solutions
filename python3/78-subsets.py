class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        current = []
        res = []

        def rec(i):
            if i == len(nums):
                res.append(current.copy())
            else:
                current.append(nums[i])
                rec(i+1)
                current.pop()
                rec(i+1)
        rec(0)
        return res
        