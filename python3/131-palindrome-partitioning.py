class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def rec(i, j):
            if j == len(s):
                if i == j:
                    res.append(cur.copy())
                    return
                else:
                    return
            if self.is_pali(s, i, j):
                cur.append(s[i:j+1])
                rec(j+1, j+1)
                cur.pop()
            
            rec(i, j+1)
        
        rec(0, 0)
        return res
    
    def is_pali(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1
        return True