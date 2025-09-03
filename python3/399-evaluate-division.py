class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(dict)

        for i in range(len(values)):
            a, b = equations[i]
            v = values[i]
            edges[a][a] = 1
            edges[b][b] = 1
            edges[a][b] = v
            edges[b][a] = 1/v

        v = set()

        def dfs(s, t, mul):
            if s == t:
                return mul
            v.add(s)
            for u in edges[s]:
                if u not in v:
                    res = dfs(u, t, mul * edges[s][u])
                    if res != -1:
                        return res
            return -1
        
        op = []
        for a, b in queries:
            if a not in edges or b not in edges:
                op.append(-1)
            else:
                v = set()
                op.append(dfs(a, b, 1))
        return op