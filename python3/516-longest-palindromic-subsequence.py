class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = [[None for _ in range(len(s))] for _ in range(len(s))] 
        def rec(i, j):
            if i == j:
                return 1
            if j == i+1:
                return 2 if s[i] == s[j] else 1
            if mem[i][j] != None:
                return mem[i][j]
            
            if s[i] == s[j]:
                mem[i][j] = rec(i+1, j-1) + 2
            else:
                mem[i][j] = max(rec(i+1, j), rec(i, j-1))
            return mem[i][j]
        
        return rec(0, len(s)-1)
        