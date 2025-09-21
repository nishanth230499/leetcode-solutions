class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        res = 0
        for num in count:
            if num + k in count:
                if k or count[num + k] > 1:
                    res += 1
        
        return res
            