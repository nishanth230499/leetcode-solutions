class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mem = [[float("inf")] * (i+1) for i in range(len(triangle))]

        mem[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j > 0:
                    mem[i][j] = min(mem[i][j], triangle[i][j] + mem[i-1][j-1])
                if j != i:
                    mem[i][j] = min(mem[i][j], triangle[i][j] + mem[i-1][j])
        
        return min(mem[-1])