class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        mem = [[None for _ in range(len(text2))] for _ in range(len(text1))]

        def rec(i, j):
            if i == -1 or j == -1:
                return 0
            if mem[i][j] != None:
                return mem[i][j]
            
            if text1[i] == text2[j]:
                mem[i][j] = rec(i-1, j-1) + 1
            else:
                mem[i][j] = max(rec(i, j-1), rec(i-1, j))
            return mem[i][j]
        # rec(len(text1)-1, len(text2)-1)
        # print(mem)
        return rec(len(text1)-1, len(text2)-1)
        