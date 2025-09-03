class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        for i in range(ceil(n**0.5) - 1, 0, -1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return n // i
        return -1