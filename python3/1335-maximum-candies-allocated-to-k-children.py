class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        return  bisect_right(range(1, max(candies)+1), -k, key=lambda a: -sum(candy//a for candy in candies))