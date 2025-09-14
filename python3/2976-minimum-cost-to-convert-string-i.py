from collections import defaultdict

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g = defaultdict(lambda: float("inf"))

        for u, v, w in zip(original, changed, cost):
            g[(u, v)] = min(g[(u, v)], w)
        
        for k in range(26):
            k = chr(ord("a") + k)
            for i in range(26):
                i = chr(ord("a") + i)
                for j in range(26):
                    j = chr(ord("a") + j)
                    if i != j and (i, k) in g and (k, j) in g:
                        g[(i, j)] = min(g[(i, j)], g[(i, k)] + g[(k, j)])

        res = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            if (s, t) in g:
                res += g[(s, t)]
            else:
                return -1
        return res