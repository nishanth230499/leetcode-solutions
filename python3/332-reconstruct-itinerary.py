class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        for u, v in sorted(tickets)[::-1]:
            edges[u].append(v)
        
        res = []
        def dfs(cur):
            while edges[cur]:
                v = edges[cur].pop()
                dfs(v)
            res.append(cur)
        
        dfs("JFK")
        return res[::-1]