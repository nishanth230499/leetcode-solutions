from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        reachability = defaultdict(dict)
        for u, v, w in edges:
            if w <= distanceThreshold:
                reachability[u][v] = w
                reachability[v][u] = w
        
        changed = True
        while changed:
            changed = False

            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        if i != k:
                            if j in reachability[i] and k in reachability[j]:
                                if reachability[i][j] + reachability[j][k] <= distanceThreshold:
                                    if k not in reachability[i] or reachability[i][j] + reachability[j][k] < reachability[i][k]:
                                        changed = True
                                        reachability[i][k] = reachability[i][j] + reachability[j][k]

        res = 0
        for i in range(1, n):
            if len(reachability[i]) <= len(reachability[res]):
                res = i
        
        return res
        