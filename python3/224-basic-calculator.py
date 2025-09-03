class Solution:
    def calculate(self, s: str) -> int:
        ans = 0

        num = 0
        sign = 1

        stack = [1]
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "(":
                stack.append(stack[-1] * sign)
                num = 0
                sign = 1
            elif c == ")":
                ans += sign * stack[-1] * num
                stack.pop()
                num = 0
                sign = 1
            elif c == "+" or c == "-":
                ans += sign * stack[-1] * num
                sign = 1 if c == "+" else -1
                num = 0
        
        return ans + sign * num
