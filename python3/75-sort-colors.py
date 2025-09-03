class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for num in nums:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            elif num == 2:
                two += 1
        
        for i in range(len(nums)):
            if zero:
                nums[i] = 0
                zero -= 1
            elif one:
                nums[i] = 1
                one -= 1
            elif two:
                nums[i] = 2
                two -= 1