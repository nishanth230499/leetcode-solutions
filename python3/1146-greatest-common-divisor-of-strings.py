class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(num1, num2):
            while num2:
                num1, num2 = num2, num1 % num2
            return num1
        return str1[:gcd(len(str1), len(str2))]