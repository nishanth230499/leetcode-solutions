class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(filter(lambda a: a, reversed(s.split(" "))))