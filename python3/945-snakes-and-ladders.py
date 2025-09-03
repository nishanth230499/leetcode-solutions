class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def move(k):
            i = (k - 1) // n
            j = (k - 1) % n
            i, j = n - i - 1, (n - j - 1 if i % 2 else j)
            return k if board[i][j] == -1 else board[i][j]
        
        vis = set()
        vis.add(1)
        q = deque()
        q.append((1, 0))

        while q:
            cur, d = q.popleft()
            if cur == n**2:
                return d
            
            for next_cur in range(cur + 1, min(cur + 6, n ** 2) + 1):
                next_cur = move(next_cur)

                if next_cur not in vis:
                    vis.add(next_cur)
                    q.append((next_cur, d + 1))
        
        return -1


