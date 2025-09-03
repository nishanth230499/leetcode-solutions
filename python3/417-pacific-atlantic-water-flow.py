class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        res = []
        mem = [[[False, False] for _ in range(n)] for _ in range(m)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        q = deque()
        for i in range(m):
            q.append((i, 0))
            visited.add((i, 0))
            mem[i][0][0] = True
        for i in range(1, n):
            q.append((0, i))
            visited.add((0, i))
            mem[0][i][0] = True
        
        while q:
            for _ in range(len(q)):
                (x, y) = q.popleft()
                for (dx, dy) in dirs:
                    i = x+dx
                    j = y+dy
                    if 0 <= i < m and 0 <= j < n and (i, j) not in visited and heights[i][j] >= heights[x][y]:
                        visited.add((i, j))
                        q.append((i, j))
                        mem[i][j][0] = True
        
        visited = set()
        q = deque()
        for i in range(m):
            q.append((i, n-1))
            visited.add((i, n-1))
            mem[i][n-1][1] = True
        for i in range(n-1):
            q.append((m-1, i))
            visited.add((m-1, i))
            mem[m-1][i][1] = True
        
        while q:
            for _ in range(len(q)):
                (x, y) = q.popleft()
                for (dx, dy) in dirs:
                    i = x+dx
                    j = y+dy
                    if 0 <= i < m and 0 <= j < n and (i, j) not in visited and heights[i][j] >= heights[x][y]:
                        visited.add((i, j))
                        q.append((i, j))
                        mem[i][j][1] = True
        
        for i in range(m):
            for j in range(n):
                if all(mem[i][j]):
                    res.append([i, j])
        
        return res