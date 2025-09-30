class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_index = 0
        min_index = len(nums) - 1

        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                min_index = min(min_index, stack.pop())
            stack.append(i)

        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                max_index = max(max_index, stack.pop())
            stack.append(i)
        
        return 0 if max_index == 0 and min_index == len(nums) - 1 else max_index - min_index + 1