class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        range = [-1, -1]
        # if nums[0]
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
                range[0] = mid
                break
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid + 1] > target):
                range[1] = mid
                break
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return range