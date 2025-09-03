class Solution:
    def grayCode(self, n: int) -> List[int]:
        def rec(i):
            if i == 1:
                return [0, 1]
            eles = rec(i-1)
            res = []
            for ele in eles:
                res.append(ele)
            for j in range(len(eles) - 1, -1, -1):
                res.append(eles[j] + (2**(i-1)))
            return res
        return rec(n)