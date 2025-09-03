class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = list(map(lambda a: (math.sqrt(a[0]**2 + a[1]**2), a), points))
        heapq.heapify(h)
        return list(map(lambda a: a[1], heapq.nsmallest(k, h)))