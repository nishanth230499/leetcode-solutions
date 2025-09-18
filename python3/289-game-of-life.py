class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        new_board = [[0] * n for _ in range(m)]

        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
            [1, 1],
            [-1, -1],
            [1, -1],
            [-1, 1]
        ]
        for i in range(m):
            for j in range(n):
                neis = 0
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj]:
                        neis += 1
                if board[i][j]:
                    if 2 <= neis <= 3:
                        new_board[i][j] = 1
                else:
                    if neis == 3:
                        new_board[i][j] = 1
        for i in range(m):
            board[i] = new_board[i]