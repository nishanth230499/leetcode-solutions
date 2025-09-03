class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def compute_days(max_w):
            w = 0
            d = 0
            for weight in weights:
                w += weight
                if w > max_w:
                    d += 1
                    w = weight
            if w:
                d += 1
            return -d

        # l = max(weights)
        # r = sum(weights)
        # while l < r:
        #     m = (l+r) // 2
        #     d = compute_days(m)
        #     if d < days:

        return bisect_left((range(max(weights), sum(weights)+1)), -days, key=compute_days) + max(weights)