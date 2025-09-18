from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats_hash = defaultdict(set)
        res = n * 2

        for i, j in reservedSeats:
            if j == 2 or j == 3:
                seats_hash[i].add(0)
            if j == 4 or j == 5:
                seats_hash[i].add(0)
                seats_hash[i].add(1)
            if j == 6 or j == 7:
                seats_hash[i].add(1)
                seats_hash[i].add(2)
            if j == 8 or j == 9:
                seats_hash[i].add(2)
        
        for i in seats_hash:
            if len(seats_hash[i]) == 3:
                res -= 2
            else:
                res -= 1
        
        return res