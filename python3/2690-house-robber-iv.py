class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def isCompatible(comp):
            last_selected = None
            count = 0
            for i in range(len(nums)):
                if (last_selected == None or last_selected != i - 1) and nums[i] <= comp:
                    count += 1
                    last_selected = i
                    if count == k:
                        return 1
            return 0
        
        sorted_nums = sorted(nums)
        return sorted_nums[bisect.bisect_left(sorted_nums, 1, key=isCompatible)]