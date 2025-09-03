class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * (i+1) for i in range(numRows)]

        for i in range(numRows):
            for j in range(i - 1):
                res[i][j+1] = res[i-1][j] + res[i-1][j+1]
        
        return res