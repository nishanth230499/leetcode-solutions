class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[None] * (len(prices)+1), [None] * (len(prices)+1)]
        def rec(i, f):
            # print(i, f)
            if(i == 0):
                return 0
            if(i == 1 and f == 1):
                return 0
            elif(i == 1 and f == 0):
                return 0
            elif(i == 2 and f == 1):
                return max(0, (prices[i-1] - prices[i-2]))
            if(dp[f][i] != None):
                return dp[f][i]
            if(f == 1):
                dp[f][i] = max(
                    rec(i-2, 0),
                    rec(i-1, 1) + (prices[i-1] - prices[i-2])
                )
                # print(i, f, dp[f][i])
                return dp[f][i]
            else:
                dp[f][i] = max(
                    rec(i-1, 1) + (prices[i-1] - prices[i-2]),
                    rec(i-1, 0)
                )
                # print(i, f, dp[f][i])
                return dp[f][i]
        
        return rec(len(prices), 0)