class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = [[None] * 5 for _ in range(len(prices))]

        def rec(i, j):
            if mem[i][j] != None:
                return mem[i][j]

            if i == 0:
                if j == 1 or j == 3:
                    return -prices[i]
                return 0

            if j == 0:
                mem[i][j] = rec(i-1, j)
            elif j == 1:
                mem[i][j] = max(rec(i-1, 0) + prices[i] - prices[i-1], rec(i-1, 1) + prices[i] - prices[i-1])
            elif j == 2:
                mem[i][j] = max(rec(i-1, 0) + prices[i] - prices[i-1], rec(i-1, 1) + prices[i] - prices[i-1], rec(i-1, 2))
            elif j == 3:
                mem[i][j] = max(rec(i-1, 2) + prices[i] - prices[i-1], rec(i-1, 3) + prices[i] - prices[i-1])
            elif j == 4:
                mem[i][j] = max(rec(i-1, 2) + prices[i] - prices[i-1], rec(i-1, 3) + prices[i] - prices[i-1], rec(i-1, 4))
            
            return mem[i][j]
        res = max(rec(len(prices) - 1, 0), rec(len(prices) - 1, 2), rec(len(prices) - 1, 4))
        return res