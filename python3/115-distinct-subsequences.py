class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mem = [[None for _ in range(len(t))] for _ in range(len(s))]

        def rec(i, j):
            if j == -1:
                return 1
            if i == -1:
                return 0
            if mem[i][j] != None:
                return mem[i][j]
            res = rec(i-1, j)
            if s[i] == t[j]:
                res += rec(i-1, j-1)
            mem[i][j] = res
            return res
        
        return rec(len(s) - 1, len(t) - 1)