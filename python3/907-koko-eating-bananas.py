class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        while r > l + 1:
            m = (l+r) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/m)
                if hrs > h:
                    l = m
                    break
            if hrs <= h:
                r = m
        return r