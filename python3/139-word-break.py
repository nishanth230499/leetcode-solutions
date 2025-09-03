class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        mem = [None for _ in range(len(s))]

        def rec(i):
            if i == len(s):
                return True
            
            if mem[i] != None:
                return mem[i]
            
            for word in wordDict:
                if s[i:].startswith(word):
                    if rec(i+len(word)):
                        mem[i] = True
                        return mem[i]
            
            mem[i] = False
            return mem[i]
        
        return rec(0)
        