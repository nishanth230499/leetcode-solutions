from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s=re.split(r"[^\w]+", paragraph.lower())
        hash_map=Counter(s)
        for i,j in hash_map.most_common():
            if i in banned or i=="":
                continue
            else:
                return i
        return ""
