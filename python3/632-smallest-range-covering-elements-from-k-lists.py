from collections import defaultdict

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []
        for i, num_array in enumerate(nums):
            for num in num_array:
                merged.append((num, i))
        
        merged.sort()

        k = len(nums)

        left = 0
        nums_count = defaultdict(int)
        count = 0

        range_left = merged[0][0]
        range_right = merged[-1][0]

        for right in range(len(merged)):
            nums_count[merged[right][1]] += 1
            if nums_count[merged[right][1]] == 1:
                count += 1
            
            while count == k:
                if merged[right][0] - merged[left][0] < range_right - range_left:
                    range_right = merged[right][0]
                    range_left = merged[left][0]
                nums_count[merged[left][1]] -= 1
                if nums_count[merged[left][1]] == 0:
                    count -= 1
                left += 1
        
        return [range_right, range_left]