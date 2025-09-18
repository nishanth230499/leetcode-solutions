class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last_hit = timeSeries[0]
        res = 0

        for hit in timeSeries[1:]:
            res += (min(hit - 1, last_hit + duration - 1) - last_hit + 1)
            last_hit = hit
        
        return res + duration