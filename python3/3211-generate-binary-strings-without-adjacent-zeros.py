class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def rec(s):
            if len(s) == n:
                res.append(s)
            else:
                if s and s[-1] == "0":
                    rec(s + "1")
                else:
                    rec(s + "1")
                    rec(s + "0")
        
        rec("")
        return res