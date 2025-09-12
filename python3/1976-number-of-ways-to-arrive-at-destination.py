import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 1000000007

        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = w
            graph[v][u] = w
        
        q = [(0, 0)]

        shortest_dist = [float("inf")] * n
        shortest_dist[0] = 0

        count = [0] * n
        count[0] = 1

        while q:
            d, u = heapq.heappop(q)

            if d == shortest_dist[u]:
                for v in graph[u]:
                    w = graph[u][v]
                    if shortest_dist[u] + w < shortest_dist[v]:
                        shortest_dist[v] = shortest_dist[u] + w
                        count[v] = count[u]
                        heapq.heappush(q, (shortest_dist[u] + w, v))
                    elif shortest_dist[u] + w == shortest_dist[v]:
                        count[v] = (count[v] + count[u]) % mod

        return count[n-1]
