class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        cur_min = nums[0]
        stack = []
        for num in nums[1:]:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][1] < num < stack[-1][0]:
                return True
            stack.append([num, cur_min])
            cur_min = min(cur_min, num)
        return False