class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        for i in range(max(len(v1), len(v2))):
            p1 = v1[i] if i < len(v1) else 0
            p2 = v2[i] if i < len(v2) else 0
            if p1 < p2:
                return -1
            if p1 > p2:
                return 1
        return 0
