class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        x, y = 0, 0
        m = len(mat)
        n = len(mat[0])

        res = []

        while True:
            while True:
                res.append(mat[x][y])
                if x == 0 or y == n - 1:
                    break
                x -= 1
                y += 1
            if y < n-1:
                y += 1
            elif x < m-1:
                x += 1
            else:
                break
            while True:
                res.append(mat[x][y])
                if y == 0 or x == m - 1:
                    break
                x += 1
                y -= 1
            if x < m - 1:
                x += 1
            elif y < n - 1:
                y += 1
            else:
                break
        
        return res

