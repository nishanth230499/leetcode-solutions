class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i])
            start = i
            while stack and stack[-1][1] >= heights[i]:
                j, h = stack.pop()
                max_area = max(max_area, h * (i - j))
                start = j
            stack.append([start, heights[i]])
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area