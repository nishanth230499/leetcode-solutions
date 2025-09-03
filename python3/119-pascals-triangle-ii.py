class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1] * (i+1) for i in range(rowIndex + 1)]

        for i in range(rowIndex + 1):
            for j in range(i - 1):
                res[i][j+1] = res[i-1][j] + res[i-1][j+1]
        
        return res[-1]