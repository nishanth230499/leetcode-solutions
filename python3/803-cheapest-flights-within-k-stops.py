class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(dict)
        for f, t, p in flights:
            edges[f][t] = p
        
        dist = [float("INF") for _ in range(n)]
        q = deque()
        q.append((0, src, 0))

        while q:
            stop_count, cur, distance = q.popleft()
            if distance < dist[cur]:
                dist[cur] = distance
                if stop_count <= k:
                    for v in edges[cur]:
                        q.append((stop_count+1, v, distance + edges[cur][v]))
        return dist[dst] if dist[dst] != float("INF") else -1
            