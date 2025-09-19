from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        unique_nums = list(counts.items())
        unique_nums.sort(key = lambda a: a[1], reverse = True)

        res = 0
        nums_deleted = 0
        for num, count in unique_nums:
            nums_deleted += count
            res += 1
            if nums_deleted >= len(arr) / 2:
                return res
        return res