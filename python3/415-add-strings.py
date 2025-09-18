class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ""
        
        carry = 0
        for i in range(len(num1)):
            total = int(num1[i]) + (int(num2[i]) if i < len(num2) else 0) + carry
            res += str(total % 10)
            carry = total // 10
        
        if carry:
            res += str(carry)

        res = res[::-1]
        return res