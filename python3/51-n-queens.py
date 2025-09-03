class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        vx = set()
        vy = set()
        vd1 = set()
        vd2 = set()

        res = []
        cur = []
        def rec(i):
            if i == n:
                cur1 = []
                for y in cur:
                    pos = ["Q" if y == j else "." for j in range(n)]
                    cur1.append("".join(pos))
                res.append(cur1)
            else:
                for j in range(n):
                    x = i
                    y = j
                    d1 = x+y
                    d2 = x+n-1-y

                    if x not in vx and y not in vy and d1 not in vd1 and d2 not in vd2:
                        cur.append(y)
                        vx.add(x)
                        vy.add(y)
                        vd1.add(d1)
                        vd2.add(d2)

                        rec(i+1)

                        vx.remove(x)
                        vy.remove(y)
                        vd1.remove(d1)
                        vd2.remove(d2)
                        cur.pop()
        rec(0)
        return res