import heapq
from collections import defaultdict

class Solution(object):
    def minimumTime(self, n, edges, disappear):
        """
        :type n: int
        :type edges: List[List[int]]
        :type disappear: List[int]
        :rtype: List[int]
        """
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        q = [(0, 0)]
        vis = set()
        answer = [float("inf")] * n

        while q:
            d, u = heapq.heappop(q)
            if u not in vis:
                vis.add(u)
                answer[u] = d

                for v, w in g[u]:
                    if v not in vis and d + w < disappear[v]:
                        heapq.heappush(q, (d + w, v))
        
        for i in range(n):
            if answer[i] == float("inf"):
                answer[i] = -1
        
        return answer