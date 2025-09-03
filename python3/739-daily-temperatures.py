class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while len(stack) and stack[-1][0] < t:
                [t1, j] = stack.pop()
                res[j] = i-j
            stack.append([t, i])
        return res