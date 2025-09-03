class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        nums = list(counts.keys())
        res = []
        self.cur = []

        def rec(i):
            if i == len(nums):
                res.append(list(self.cur))
            else:
                rec(i+1)
                for j in range(counts[nums[i]]):
                    self.cur.append(nums[i])
                    rec(i+1)
                self.cur = self.cur[:-counts[nums[i]]]

        rec(0)
        return res