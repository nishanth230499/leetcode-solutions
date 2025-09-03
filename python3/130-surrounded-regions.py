class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        q = deque()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(m):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "o"
            if board[i][n-1] == 'O':
                q.append((i, n-1))
                board[i][n-1] = "o"
        for i in range(1, n-1):
            if board[0][i] == "O":
                q.append((0, i))
                board[0][i] = "o"
            if board[m-1][i] == "O":
                q.append((m-1, i))
                board[m-1][i] = "o"
        
        while q:
            for _ in range(len(q)):
                (x, y) = q.popleft()
                for (dx, dy) in dirs:
                    i = x+dx
                    j = y+dy
                    if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                        board[i][j] = "o"
                        q.append((i, j))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "o":
                    board[i][j] = "O"