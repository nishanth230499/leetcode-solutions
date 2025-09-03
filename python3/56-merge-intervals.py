class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort = []
        for interval in intervals:
            bisect.insort(sort, interval)
        
        res = []
        for interval in sort:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res