class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            print(low, mid, high)
            if nums[mid] == target:
                return mid
            if nums[low] == target:
                return low
            if nums[high] == target:
                return high
            if nums[mid] > nums[low]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target < nums[mid] or target > nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            

        return -1
        