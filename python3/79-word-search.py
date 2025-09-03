class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m = len(board)
        n = len(board[0])

        visited = set()
        
        def rec(x, y, i):
            if i == len(word):
                return True
            soln = False
            for [dx, dy] in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[i] and f"{nx},{ny}" not in visited:
                    visited.add(f"{nx},{ny}")
                    soln = soln or rec(nx, ny, i+1)
                    visited.remove(f"{nx},{ny}")
            return soln
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited.add(f"{i},{j}")
                    if rec(i, j, 1):
                        return True
                    visited.remove(f"{i},{j}")
        return False