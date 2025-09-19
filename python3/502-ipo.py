class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_sorted = [(-profits[i], capital[i]) for i in range(len(profits))]
        capital_sorted.sort(key = lambda a: a[1])
        
        q = []
        i = 0

        for _ in range(k):
            while i < len(capital_sorted) and capital_sorted[i][1] <= w:
                heapq.heappush(q, capital_sorted[i])
                i += 1
            if not q:
                break
            w += -heapq.heappop(q)[0]
        
        return w
        
