class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            while stack and stack[-1] > c and k:
                stack.pop()
                k -= 1
            stack.append(c)

        if k:
            stack = stack[:-k]

        return "".join(stack).lstrip("0") or "0"
