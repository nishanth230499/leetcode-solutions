class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = defaultdict(set)

        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        
        def rec(cur, par):
            res = 0
            for v in g[cur]:
                if v != par:
                    t = rec(v, cur)
                    if t or hasApple[v]:
                        t += 2
                    res += t
            
            return res
        
        return rec(0, None)