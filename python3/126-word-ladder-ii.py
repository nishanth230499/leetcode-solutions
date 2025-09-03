from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def is_nei(a, b):
            if len(a) != len(b):
                return False
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        distance = {}
        pen = defaultdict(set)
        q = deque([(0, beginWord, None)])

        while q:
            (d, cur, parent) = q.popleft()
            if cur not in distance:
                distance[cur] = d
                if cur != endWord:
                    for word in wordList:
                        if word != parent and is_nei(word, cur):
                            q.append((d+1, word, cur))
            if distance[cur] == d:
                pen[cur].add(parent)
        
        q = deque([[endWord]])
        res = []

        while q:
            l = q.popleft()
            if l[-1] == beginWord:
                res.append(l[::-1])
            else:
                for word in pen[l[-1]]:
                    q.append(l + [word])
        return res
        


