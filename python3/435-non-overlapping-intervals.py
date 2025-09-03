class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a: a[1])
        cur = intervals[0][0] - 1
        used = 0
        for interval in intervals:
            if cur <= interval[0]:
                used += 1
                cur = interval[1]
        return len(intervals) - used