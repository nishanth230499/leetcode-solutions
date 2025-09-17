class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        width = sum(wall[0])

        edges = defaultdict(int)

        for row in wall:
            total = 0
            for brick in row:
                total += brick
                edges[total] += 1
            edges[total] -= 1
        
        min_cut = float("inf")
        for edge in edges:
            if edge != width:
                min_cut = min(min_cut, len(wall) - edges[edge])
        
        return len(wall) if min_cut == float("inf") else min_cut