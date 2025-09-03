class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            print(low, mid, high)
            if nums[mid] == target or (nums[mid] > target and nums[mid-1] < target):
                return mid
            if nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return -1


        