class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        fst_col_zero = any(map(lambda a: a[0] == 0, matrix))
        fst_row_zero = any(map(lambda a: a == 0, matrix[0]))
        for row in matrix[1:]:
            if any(map(lambda a: a == 0, row)):
                row[0] = 0
        for i in range(1, len(matrix[0])):
            if any(map(lambda a: a[i] == 0, matrix)):
                matrix[0][i] = 0
        for row in matrix[1:]:
            if row[0] == 0:
                for j in range(len(row)):
                    row[j] = 0
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        if fst_col_zero:
            for row in matrix:
                row[0] = 0
        if fst_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0