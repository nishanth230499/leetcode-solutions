class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = list(map(lambda a: -a, stones))
        heapq.heapify(h)
        while len(h) > 1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            x = abs(x-y)
            if x != 0:
                heapq.heappush(h, -x)
        if len(h):
            return -h[0]
        else:
            return 0