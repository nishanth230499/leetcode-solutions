class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = [[None for _ in range(len(s))] for _ in range(len(s))]

        def rec(i, j):
            if j - i == 0:
                return True
            if j - i == 1:
                return s[i] == s[j]
            if mem[i][j] != None:
                return mem[i][j]
            if s[i] == s[j]:
                mem[i][j] = rec(i+1, j-1)
            else:
                mem[i][j] = False
            return mem[i][j]
        
        arr = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if rec(i, j):
                    arr += 1
        return arr
        