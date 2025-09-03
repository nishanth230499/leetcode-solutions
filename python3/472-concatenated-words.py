class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        failing_set = set()

        def dfs(sub):
            if sub in words_set:
                return True
            if sub in failing_set:
                return False
            for i in range(1, len(sub) + 1):
                if sub[:i] in words_set and dfs(sub[i:]):
                    return True
            failing_set.add(sub)
            return False

        res = []
        for word in words:
            words_set.remove(word)
            if dfs(word):
                res.append(word)
            words_set.add(word)
        
        return res

