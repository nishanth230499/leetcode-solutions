class Solution:
    def numSquares(self, n: int) -> int:
        mem = {}
        def rec(i):
            if i == 0:
                return 0
            if i in mem:
                return mem[i]
            j = 1
            res = float("inf")
            while i - j ** 2 >= 0:
                res = min(res, rec(i - j ** 2))
                j += 1
            mem[i] = res + 1
            return res + 1
        
        return rec(n)