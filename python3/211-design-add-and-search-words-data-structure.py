class TreeNode:
    def __init__(self):
        self.children = {}
        self.ends = False

class WordDictionary:

    def __init__(self):
        self.tree = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.tree
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.ends = True

    def search(self, word: str) -> bool:
        self.cur = self.tree
        def rec(i):
            if i == len(word):
                return self.cur.ends
            if word[i] == ".":
                sol = False
                mem_cur = self.cur
                for c in self.cur.children:
                    self.cur = self.cur.children[c]
                    sol = sol or rec(i+1)
                    self.cur = mem_cur
                return sol
            elif word[i] in self.cur.children:
                self.cur = self.cur.children[word[i]]
                return rec(i+1)
            else:
                return False
        
        return rec(0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)