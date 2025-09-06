class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = set()
        res = set()
        for i in range(10, len(s) + 1):
            seq = s[i-10:i]
            if seq in visited:
                res.add(seq)a
            else:
                visited.add(seq)
        
        return list(res)