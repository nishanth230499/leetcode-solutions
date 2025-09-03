class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        sign = x / abs(x)
        x = abs(x)
        res = 0
        while x:
            res = res * 10 + (x % 10)
            x = x // 10
        res = sign * res
        return 0 if res < -1 * (2 ** 31) or res >= 2 ** 31 else res

        