class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1c = [0] * 26
        s2c = [0] * 26
        for i in range(len(s1)):
            s1c[ord(s1[i]) - ord("a")] += 1
            s2c[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1c[i] == s2c[i] else 0
        
        l = 0
        for i in range(len(s1), len(s2)):
            # print(matches)
            # print(s1c)
            # print(s2c)
            if matches == 26:
                return True
            index = ord(s2[i]) - ord("a")
            s2c[index] += 1
            if s2c[index] == s1c[index]:
                matches += 1
            if s2c[index] == 1 + s1c[index]:
                matches -= 1
            
            index = ord(s2[i - len(s1)]) - ord("a")
            s2c[index] -= 1
            if s2c[index] == s1c[index]:
                matches += 1
            if s2c[index] == s1c[index] - 1:
                matches -= 1
        
        return matches == 26