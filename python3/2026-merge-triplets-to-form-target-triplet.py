class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0, 0, 0]
        for tri in triplets:
            if tri[0] <= target[0] and tri[1] <= target[1] and tri[2] <= target[2]:
                cur[0] = max(cur[0], tri[0])
                cur[1] = max(cur[1], tri[1])
                cur[2] = max(cur[2], tri[2])
        
        if cur[0] == target[0] and cur[1] == target[1] and cur[2] == target[2]:
            return True
        return False