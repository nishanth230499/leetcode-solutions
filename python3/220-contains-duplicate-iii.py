class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}

        for i, num in enumerate(nums):
            bucket_index = num // (valueDiff + 1)

            if bucket_index - 1 in buckets and i - buckets[bucket_index - 1][0] <= indexDiff and abs(buckets[bucket_index - 1][1] - num) <= valueDiff:
                return True

            if bucket_index in buckets and i - buckets[bucket_index][0] <= indexDiff and abs(buckets[bucket_index][1] - num) <= valueDiff:
                return True
            
            if bucket_index + 1 in buckets and i - buckets[bucket_index + 1][0] <= indexDiff and abs(buckets[bucket_index + 1][1] - num) <= valueDiff:
                return True
            
            buckets[bucket_index] = (i, num)
        
        return False