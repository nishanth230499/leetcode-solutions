class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        q = [(arr[0] / arr[-1], 0, len(arr) - 1)]
        vis = set()
        vis.add((0, len(arr) - 1))

        for _ in range(k - 1):
            _, s, e = heapq.heappop(q)
            if s != e:
                opt1 = (arr[s + 1] / arr[e], s + 1, e)
                if opt1 not in vis:
                    vis.add(opt1)
                    heapq.heappush(q, opt1)
                opt2 = (arr[s] / arr[e - 1], s, e - 1)
                if opt2 not in vis:
                    vis.add(opt2)
                    heapq.heappush(q, opt2)
        
        _, s, e = heapq.heappop(q)

        return [arr[s], arr[e]]
