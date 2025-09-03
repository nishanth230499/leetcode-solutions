class Solution:
    def numDecodings(self, s: str) -> int:
        pre_res = 1
        pre_pre_res = 1
        for i in range(len(s)):
            res = 0
            if int(s[i]) != 0:
                res += pre_res
            if i > 0 and int(s[i-1]) != 0 and 1 <= int(s[i-1:i+1]) <= 26:
                res += pre_pre_res
            pre_pre_res = pre_res
            pre_res = res
        return res