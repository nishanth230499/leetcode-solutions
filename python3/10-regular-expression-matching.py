class Solution(object):
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.cache = [[None for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        return self.c_is_match(s, p)
    
    def c_is_match(self, s, p):
        if self.cache[len(s)][len(p)] is not None:
            return self.cache[len(s)][len(p)]
        if s == "" and p == "":
            self.cache[len(s)][len(p)] = True
            return True
        if p == "":
            self.cache[len(s)][len(p)] = False
            return False
        # if len(p) > 1 and p[1] == "*":
        #     if s == "":
        #         return self.isMatch(s, p[2:])
        #     if p[0] == "." or s[0] == p[0]:
        #         return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
        #     return self.isMatch(s, p[2:])
        # if s == "":
        #     return False
        # if s[0] == p[0] or p[0] == ".":
        #     return self.isMatch(s[1:], p[1:])
        # return False

        if p[-1] == "*":
            if self.c_is_match(s, p[:-2]):
                self.cache[len(s)][len(p)] = True
                return True
            if s == "":
                self.cache[len(s)][len(p)] = False
                return False
            if p[-2] == s[-1] or p[-2] == ".":
                if self.c_is_match(s[:-1], p):
                    self.cache[len(s)][len(p)] = True
                    return True
                else:
                    self.cache[len(s)][len(p)] = False
                    return False
            else:
                self.cache[len(s)][len(p)] = False
                return False
        if s == "":
            self.cache[len(s)][len(p)] = False
            return False
        if s[-1] == p[-1] or p[-1] == ".":
            if self.c_is_match(s[:-1], p[:-1]):
                self.cache[len(s)][len(p)] = True
                return True
            else:
                self.cache[len(s)][len(p)] = False
                return False
        self.cache[len(s)][len(p)] = False
        return False
            

        