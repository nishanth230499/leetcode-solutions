class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        carry = 0
        sum = ""
        for i in range(1, max_len + 1):
            digit_sum = (int(a[len(a) - i]) if len(a) - i >= 0 else 0) + (int(b[len(b) - i]) if len(b) - i >= 0 else 0) + carry
            sum = str(digit_sum % 2) + sum
            carry = digit_sum // 2
        return "1"+sum if carry else sum
