class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        min_ele = min(nums)
        max_ele = max(nums)

        bucket_size = max(1, (max_ele - min_ele) // len(nums))
        buckets_count = (max_ele - min_ele) // bucket_size + 1

        buckets = [None] * buckets_count

        for num in nums:
            bucket_index = (num - min_ele) // bucket_size
            if buckets[bucket_index]:
                buckets[bucket_index]["min"] = min(buckets[bucket_index]["min"], num)
                buckets[bucket_index]["max"] = max(buckets[bucket_index]["max"], num)
            else:
                buckets[bucket_index] = {"min": num, "max": num}
        
        max_diff = 0
        prev_bucket_max = min_ele

        for bucket in buckets:
            if bucket:
                max_diff = max(max_diff, bucket["min"] - prev_bucket_max)
                prev_bucket_max = bucket["max"]
        
        return max_diff