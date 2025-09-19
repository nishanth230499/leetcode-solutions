class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        w_q_sorted = [(-quality[i], wage[i] / quality[i]) for i in range(len(wage))]
        w_q_sorted.sort(key = lambda a: a[1])
        
        res = float("inf")
        q = []
        total_quality = 0

        for i in range(len(w_q_sorted)):
            heapq.heappush(q, w_q_sorted[i])
            total_quality += -w_q_sorted[i][0]

            if len(q) > k:
                total_quality -= -heapq.heappop(q)[0]
            
            if len(q) == k:
                res = min(res, w_q_sorted[i][1] * total_quality)
        
        return res