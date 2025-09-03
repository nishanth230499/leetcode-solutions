class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        mem = [[None for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        def rec(i, j):
            if i == 0 and j == 0:
                return True
            if mem[i][j] == None:
                mem[i][j] = (i > 0 and s1[i-1] == s3[i+j-1] and rec(i-1, j)) or (j > 0 and s2[j-1] == s3[i+j-1] and rec(i, j-1))
            return mem[i][j]
        return rec(len(s1), len(s2))