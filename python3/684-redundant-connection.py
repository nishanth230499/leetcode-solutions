class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        e = {}

        for [i, j] in edges:
            if i not in e:
                e[i] = set()
            if j not in e:
                e[j] = set()
            e[i].add(j)
            e[j].add(i)
        
        cycle = set()
        order = []

        def dfs(i, prev):
            if i in cycle:
                return i
            cycle.add(i)
            order.append(i)
            for j in e[i]:
                if j != prev:
                    sol = dfs(j, i)
                    if sol:
                        return sol
            cycle.remove(i)
            order.pop()
            return False
        
        v = dfs(1, 0)
        i = order.index(v)
        order = order[i:]
        cycle = set(order)
        
        for i in range(len(edges)-1, -1, -1):
            if edges[i][0] in cycle and edges[i][1] in cycle:
                return edges[i]