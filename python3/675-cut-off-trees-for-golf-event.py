class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])
        dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        points = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    points.append((forest[i][j], i, j))
        
        points.sort()
        
        cur = (0, 0)
        steps = 0
        for (_, x2, y2) in points:
            q = deque()
            q.append(((cur[0], cur[1], 0)))
            vis = set()
            while q:
                x, y, d = q.popleft()
                if x == x2 and y == y2:
                    forest[x2][y2] = 1
                    steps += d
                    cur = (x2, y2)
                    break
                for dx, dy in dirs:
                    x1, y1 = x + dx, y + dy
                    if 0 <= x1 < m and 0 <= y1 < n and forest[x1][y1] >= 1 and (x1, y1) not in vis:
                        vis.add((x1, y1))
                        q.append((x1, y1, d + 1))
            else:
                return -1
        return steps
        

