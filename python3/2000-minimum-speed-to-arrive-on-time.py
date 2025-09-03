class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        return -1 if hour <= len(dist)-1 else bisect_left(range(1, max(max(dist[:-1]) if len(dist[:-1]) else 0, ceil(dist[-1] / (hour-len(dist)+1)) )), -hour, key=lambda a: (-sum(ceil(d/a) for d in dist[:-1]) - dist[-1]/a)) + 1
        

        