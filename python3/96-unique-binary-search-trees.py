class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = [None for _ in range(n+1)]

        def rec(i):
            if i == 1:
                return 1
            if mem[i] != None:
                return mem[i]
            
            res = 0
            res += 2*rec(i-1)

            for j in range(1, i-1):
                res += rec(j) * rec(i-j-1)
            
            mem[i] = res
            return mem[i]
        
        return rec(n)