class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = re.sub(r"(\*)\1+", r"\1", p)
        mem = {}
        def rec(i, j):
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            if i in mem and j in mem[i]:
                return mem[i][j]
            if p[j] == "?":
                if i == len(s):
                    ans = False
                else:
                    ans = rec(i+1, j+1)
            elif p[j] == "*":
                ans = False
                for k in range(i, len(s)+1):
                    if rec(k, j+1):
                        ans = True
                        break
            elif i == len(s):
                ans = False
            elif s[i] == p[j]:
                ans = rec(i+1, j+1)
            else:
                ans = False
            if i not in mem:
                mem[i] = {}
            mem[i][j] = ans
            return ans
        
        return rec(0, 0)
            
        
        