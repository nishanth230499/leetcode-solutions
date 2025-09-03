class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums)

        while high > low:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True

            if nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]:
                if nums[mid] < target <= nums[high-1]:
                    low = mid + 1
                else:
                    high = mid
            else:
                low += 1

        return False