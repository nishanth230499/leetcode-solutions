class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = self.myPow(x, n//2)
        res = res * res
        if n % 2:
            res = res * x
        return res