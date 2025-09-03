from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        q = list(map(lambda a: (-a[1], a[0]), counts.items()))
        heapq.heapify(q)
        return(list(map(lambda a: a[1], heapq.nsmallest(k, q))))