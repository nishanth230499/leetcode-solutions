class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = defaultdict(set)
        res = [0] * n

        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        def rec(cur, par):
            count = [0] * 26
            
            for v in g[cur]:
                if v != par:
                    child_count = rec(v, cur)
                    for i in range(26):
                        count[i] += child_count[i]
            
            count[ord(labels[cur]) - ord("a")] += 1
            res[cur] = count[ord(labels[cur]) - ord("a")]
            return count
            
        rec(0, None)

        return res