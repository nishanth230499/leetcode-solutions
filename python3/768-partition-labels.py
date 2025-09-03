class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        rem = set()
        res = []
        counter = 0
        for c in s:
            count[c] -= 1
            counter += 1
            rem.add(c)
            if count[c] == 0:
                rem.remove(c)
            if not rem:
                res.append(counter)
                counter = 0
        return res