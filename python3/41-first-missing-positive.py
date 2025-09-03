class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if index >= 0 and index < len(nums):
                if nums[index] > 0:
                    nums[index] *= -1
                if nums[index] == 0:
                    nums[index] = float("-inf")
        # print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        return len(nums)+1