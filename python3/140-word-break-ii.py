class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        self.words = ""
        def dfs(i):
            if i == len(s):
                res.append(self.words[:-1])
                return
            for word in wordDict:
                if i+len(word) <= len(s) and word == s[i:i+len(word)]:
                    self.words += word
                    self.words += " "
                    dfs(i+len(word))
                    self.words = self.words[:-len(word)-1]
        
        dfs(0)
        return res
