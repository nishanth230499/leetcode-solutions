import heapq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff(a, b):
            if len(a) != len(b):
                return False
            c = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    c += 1
                    if c > 1:
                        return False
            return c == 1
        
        q = []
        v = set()
        heapq.heappush(q, (0, beginWord))
        while q:
            d, cur = heapq.heappop(q)
            if cur == endWord:
                return d + 1
            if cur not in v:
                v.add(cur)
                for word in wordList:
                    if word not in v and diff(cur, word):
                        heapq.heappush(q, (d+1, word))
        return 0