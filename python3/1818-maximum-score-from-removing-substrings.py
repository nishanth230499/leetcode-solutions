class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0

        def solve(subs, pattern, reward, res):
            stack = []
            for c in subs:
                if stack and stack[-1] == pattern[0] and c == pattern[1]:
                    res += reward
                    stack.pop()
                else:
                    stack.append(c)
            return "".join(stack), res

        
        if x > y:
            rem, res = solve(s, "ab", x, res)
            _, res = solve(rem, "ba", y, res)
        else:
            rem, res = solve(s, "ba", y, res)
            _, res = solve(rem, "ab", x, res)
        return res
        