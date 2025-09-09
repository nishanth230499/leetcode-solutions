
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_count = [0] * 26
        for c in p:
            p_count[ord(c) - ord("a")] += 1
        
        p_count = ",".join(map(str, p_count))
        c_count = [0] * 26

        res = []
        for i in range(len(p)):
            c_count[ord(s[i]) - ord("a")] += 1

        if ",".join(map(str, c_count)) == p_count:
            res.append(0)
        
        left = 0
        right = len(p) - 1
        while right < len(s) - 1:
            right += 1
            c_count[ord(s[right]) - ord("a")] += 1
            c_count[ord(s[left]) - ord("a")] -= 1
            left += 1

            if ",".join(map(str, c_count)) == p_count:
                res.append(left)

        return res
