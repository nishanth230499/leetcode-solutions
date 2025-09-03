class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            carry = ((a & b) << 1) & mask
            a = (a^b) & mask
            b = carry
        return -((~a + 1) & mask) if (a >> 31) else a