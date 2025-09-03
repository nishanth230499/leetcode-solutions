from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edges = defaultdict(set)
        for [u, v] in connections:
            edges[u].add(v)
            edges[v].add(u)
        
        visited = set()
        rank = [0] * n
        min_rank = [0] * n
        count = 0
        critical = []

        def dfs(cur, parent):
            nonlocal count
            if cur in visited:
                return
            visited.add(cur)
            rank[cur] = count
            min_rank[cur] = count
            count += 1

            for nei in edges[cur]:
                if nei == parent:
                    continue
                
                dfs(nei, cur)
                min_rank[cur] = min(min_rank[cur], min_rank[nei])

                if min_rank[nei] > rank[cur]:
                    critical.append([nei, cur])
        
        dfs(0, None)
        return critical
