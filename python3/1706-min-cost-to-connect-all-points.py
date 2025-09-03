class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calc_dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        visited = [False for _ in points]
        q = [(calc_dist(points[0], points[i]), i) for i in range(len(points))]
        heapq.heapify(q)
        total_dist = 0

        while q:
            dist, cur = heapq.heappop(q)
            if not visited[cur]:
                total_dist += dist
                visited[cur] = True
                for i, point in enumerate(points):
                    if i != cur and not visited[i]:
                        heapq.heappush(q, (calc_dist(points[cur], points[i]), i))
        
        return total_dist