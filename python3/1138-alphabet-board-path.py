class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        cur_i, cur_j = 0, 0
        res = ""

        for c in target:
            v = ord(c) - ord("a")
            vi = v // 5
            vj = v % 5

            di = vi - cur_i
            dj = vj - cur_j

            if di < 0:
                for _ in range(-di):
                    res += "U"
            for _ in range(abs(dj)):
                res += "R" if dj > 0 else "L"
            if di > 0:
                for _ in range(di):
                    res += "D"

            res += "!"
            cur_i, cur_j = vi, vj
        
        return res