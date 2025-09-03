class TreeNode:
    def __init__(self):
        self.ends = False
        self.children = {}

class Trie:

    def __init__(self):
        self.tree = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.tree
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.ends = True

    def search(self, word: str) -> bool:
        cur = self.tree
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.ends

    def startsWith(self, prefix: str) -> bool:
        cur = self.tree
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)