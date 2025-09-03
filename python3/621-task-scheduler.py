class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        order = []
        remaining = Counter(tasks)
        waitingp = set()
        h = list(map(lambda a: (-remaining[a], a), remaining.keys()))
        heapq.heapify(h)

        while len(waitingp) or len(h):
            if len(h):
                (c, p) = heapq.heappop(h)
                remaining[p] -= 1
                if remaining[p] > 0:
                    waitingp.add(p)
                order.append(p)
            else:
                order.append(None)
            if len(order) > n and order[-n-1]:
                p = order[-n-1]
                if remaining[p] > 0:
                    waitingp.remove(p)
                    heapq.heappush(h, (-remaining[p], p))
        return len(order)