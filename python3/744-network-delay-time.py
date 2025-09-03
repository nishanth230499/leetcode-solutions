class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {u: {} for u in range(1, n+1)}
        for u, v, t in times:
            edges[u][v] = t
        visited = set()
        reach_time = [-1] * n
        # visited.add(k)
        # reach_time[k-1] = 0
        q = []
        heapq.heappush(q, (0, k))
        total_time = 0
        while q:
            cur_t, cur = heapq.heappop(q)
            if cur not in visited:
                total_time = cur_t
                visited.add(cur)
                reach_time[cur-1] = cur_t
                for v in edges[cur]:
                    if v not in visited:
                        heapq.heappush(q, (cur_t + edges[cur][v], v))
        return total_time if len(visited) == n else -1