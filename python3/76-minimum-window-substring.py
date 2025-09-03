class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def get_index(c):
            if c.isupper():
                return ord(c) - ord('A') + 26
            else:
                return ord(c) - ord('a')
        
        if len(s) < len(t):
            return ""
        
        s_count = [0] * 52
        t_count = [0] * 52
        for i in range(len(t)):
            t_count[get_index(t[i])] += 1
            s_count[get_index(s[i])] += 1
        
        matches = 0
        for i in range(52):
            matches += 1 if s_count[i] >= t_count[i] else 0

        l = 0
        res = s[:len(t)] if matches == 52 else None
        for r in range(len(t), len(s)):
            index = get_index(s[r])
            s_count[index] += 1
            if s_count[index] == t_count[index]:
                matches += 1
            
            if res != None and r-l+1 >= len(res):
                index = get_index(s[l])
                s_count[index] -= 1
                if s_count[index] == t_count[index] - 1:
                    matches -= 1
                l += 1
            
            while matches == 52:
                res = s[l:r+1]
                index = get_index(s[l])
                s_count[index] -= 1
                if s_count[index] == t_count[index] - 1:
                    matches -= 1
                l += 1
        return res or ""
            



        