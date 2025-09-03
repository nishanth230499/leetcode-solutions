class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = len(matrix[0])
        for row in matrix:
            right = bisect_right(row, target, hi=right)
            if right == 0:
                return False
            if row[right - 1] == target:
                return True
            