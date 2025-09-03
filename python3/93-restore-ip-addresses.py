class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def rec(i, j):
            if i == 0 and j == 0:
                return [""]
            if i == 0 or j == 0:
                return []
            res = []
            for k in range(1, 4):
                if i-k >= 0:
                    sub_str = s[i-k:i]
                    # print(i-k, i, sub_str, int(sub_str))
                    if int(sub_str) <= 255 and (k == 1 or sub_str[0] != "0"):
                        sub_res = rec(i-k, j-1)
                        for ele in sub_res:
                            res.append(ele + "." + sub_str)
            return res
        
        return list(map(lambda a: a[1:], rec(len(s), 4)))