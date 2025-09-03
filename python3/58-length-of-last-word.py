class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = list(filter(lambda a: a != "", s.split()))
        return len(words[-1])