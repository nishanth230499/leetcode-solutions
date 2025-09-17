class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        total = 0
        res = 0
        first_seen = {}

        for i, hour in enumerate(hours):
            if hour > 8:
                total += 1
            else:
                total -= 1
            if total > 0:
                res = max(res, i + 1)
            else:
                if total - 1 in first_seen:
                    res = max(res, i - first_seen[total - 1])
            if total not in first_seen:
                first_seen[total] = i
        
        return res

