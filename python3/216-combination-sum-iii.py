class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def rec(k, n, i):
            if i == 1:
                if k == 0 and n == 0:
                    return [[]]
                if k == 1 and n == 1:
                    return [[1]]
                return []
            
            res = rec(k, n, i-1)
            if n >= i:
                res.extend(list(map(lambda a: a+[i], rec(k-1, n-i, i-1))))
            return res
        return rec(k, n, 9)
