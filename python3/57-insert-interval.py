class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = bisect.bisect(intervals, newInterval)
        if i != 0 and newInterval[0] <= intervals[i-1][1]:
            intervals[i-1][1] = max(newInterval[1], intervals[i-1][1])
            i = i-1
        else:
            intervals.insert(i, newInterval)
        
        while i < len(intervals)-1 and intervals[i+1][0] <= intervals[i][1]:
            intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
            intervals.pop(i+1)
        
        return intervals