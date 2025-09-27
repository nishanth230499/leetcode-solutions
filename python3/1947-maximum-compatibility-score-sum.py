class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def comp(a, b):
            res = 0
            for i, j in zip(a, b):
                if i == j:
                    res += 1
            return res
        
        alloted_mentors = set()
        self.max_score = 0
        self.score = 0

        def rec(i):
            if i == len(students):
                self.max_score = max(self.max_score, self.score)
                return
            for j in range(len(mentors)):
                if j not in alloted_mentors:
                    alloted_mentors.add(j)
                    c = comp(students[i], mentors[j])
                    self.score += c
                    rec(i + 1)
                    self.score -= c
                    alloted_mentors.remove(j)
            
        rec(0)
        return self.max_score
