class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_square(i):
            res = 0
            while i:
                res += (i%10)**2
                i //= 10
            return res
        
        v = set()
        v.add(n)
        while True:
            n = sum_square(n)
            if n == 1:
                return True
            if n in v:
                return False
            v.add(n)