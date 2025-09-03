import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(lambda: 0)
        for c in s:
            count[c] += 1
        q = list(map(lambda a: (-a[1], a[0], a[1]), count.items()))
        heapq.heapify(q)
        prev = None
        res = ""
        while q:
            _, ch1, co1 = heapq.heappop(q)
            if ch1 != prev:
                res += ch1
                prev = ch1
                if co1 != 1:
                    heapq.heappush(q, (-co1+1, ch1, co1-1))
            else:
                if not q:
                    return ""
                _, ch2, co2 = heapq.heappop(q)
                res += ch2
                prev = ch2
                if co2 != 1:
                    heapq.heappush(q, (-co2+1, ch2, co2-1))
                heapq.heappush(q, (-co1, ch1, co1))
        return res
            
            

