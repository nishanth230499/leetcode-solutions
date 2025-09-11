from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        adj = defaultdict(dict)
        for u, v, cnt in edges:
            adj[u][v] = [cnt, 0]
            adj[v][u] = [cnt, 0]
        
        q = [[0, 0]]
        vis = set()
        res = 0

        while q:
            d, u = heapq.heappop(q)
            if u not in vis:
                vis.add(u)
                res += 1
                for v in adj[u]:
                    cnt, occupied = adj[u][v]
                    inc = min(cnt - occupied, maxMoves - d)
                    if inc > 0 or cnt == 0:
                        res += inc
                        adj[u][v][1] += inc
                        adj[v][u][1] += inc
                        if cnt < maxMoves - d:
                            heapq.heappush(q, [d + cnt + 1, v])
        
        return res

