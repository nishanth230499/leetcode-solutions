class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        h = []
        res = {}
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l = intervals[i][0]
                r = intervals[i][1]
                heapq.heappush(h, (r-l+1, r))
                i += 1
            
            while h and h[0][1] < q:
                heapq.heappop(h)
            
            res[q] = h[0][0] if h else -1
        
        res1 = [res[q] for q in queries]
        return res1