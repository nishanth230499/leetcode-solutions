import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            heapq.heappush(q, diff)
            if len(q) > ladders:
                min_diff = heapq.heappop(q)
                bricks -= min_diff
                if bricks < 0:
                    return i
        return len(heights) - 1
                