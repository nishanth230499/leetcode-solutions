from collections import defaultdict
import heapq

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        edges.sort(key = lambda a: a[2])

        g = defaultdict(list)

        for u, v, w in edges:
            g[v].append((u, w))
        
        res = 0
        q = [(0, 0)]
        vis = set()

        while q:
            w, u = heapq.heappop(q)
            if u not in vis:
                vis.add(u)
                res = max(res, w)
                if len(vis) == n:
                    return res
                
                for v, w in g[u]:
                    if v not in vis:
                        heapq.heappush(q, (w, v))
        return -1