class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[None for _ in range(n)] for _ in range(n)]

        i = 0
        j = 0
        di = 0
        dj = 1
        num = 1

        while num <= n * n:
            nums[i][j] = num
            num += 1
            if not(0 <= i + di < n and 0 <= j + dj < n and nums[i+di][j+dj] == None):
                di, dj = dj, -di
            i += di
            j += dj
        return nums
