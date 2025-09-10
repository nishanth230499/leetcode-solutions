from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0

        for num in counts:
            if num + 1 in counts:
                res = max(res, counts[num] + counts[num + 1])
        
        return res