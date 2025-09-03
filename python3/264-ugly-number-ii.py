import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        v = set()
        for _ in range(n):
            cur = heapq.heappop(heap)
            for m in [2, 3, 5]:
                next_num = cur * m
                if next_num not in v:
                    heapq.heappush(heap, next_num)
                    v.add(next_num)
        
        return cur