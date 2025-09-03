class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        high = prices[0]
        max_diff = 0
        for num in prices:
            if num < least:
                least = num
                high = num
            elif num > high:
                high = num
                max_diff = max(max_diff, high-least)
        return max_diff
