class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = set()

        def rec(i, cur):
            if i == len(nums):
                if len(cur) > 1:
                    self.res.add(tuple(cur))
                return
            if not cur or cur[-1] <= nums[i]:
                cur.append(nums[i])
                rec(i+1, cur)
                cur.pop()
            
            rec(i+1, cur)
        
        rec(0, [])

        return [list(x) for x in self.res]