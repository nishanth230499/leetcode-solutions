class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        mem = [[None for _ in range(len(word2))] for _ in range(len(word1))]

        def rec(i, j):
            if i == -1:
                return j+1
            if j == -1:
                return i+1
            
            if mem[i][j] != None:
                return mem[i][j]
            
            if word1[i] == word2[j]:
                mem[i][j] = rec(i-1, j-1)
            else:
                mem[i][j] = min(rec(i-1, j), rec(i, j-1), rec(i-1, j-1)) + 1
            
            return mem[i][j]
        
        return rec(len(word1)-1, len(word2)-1)
        