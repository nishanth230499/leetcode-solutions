from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = defaultdict(int)
        
        for i in range(min(k+1, len(nums))):
            count[nums[i]] += 1
            if count[nums[i]] == 2:
                return True

        for i in range(k+1, len(nums)):
            count[nums[i]] += 1
            count[nums[i-k-1]] -= 1
            if count[nums[i]] == 2:
                return True
        
        return False