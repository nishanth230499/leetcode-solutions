from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(max_unique_chars):
            left = 0
            unique_chars = 0
            char_count = defaultdict(int)
            chars_ge_k = 0

            max_count = 0

            for right in range(0, len(s)):
                if char_count[s[right]] == 0:
                    unique_chars += 1
                char_count[s[right]] += 1
                if char_count[s[right]] == k:
                    chars_ge_k += 1
                
                while unique_chars > max_unique_chars:
                    if char_count[s[left]] == k:
                        chars_ge_k -= 1
                    char_count[s[left]] -= 1
                    if char_count[s[left]] == 0:
                        unique_chars -= 1
                    left += 1
                
                if chars_ge_k == unique_chars:
                    max_count = max(max_count, right - left + 1)
            return max_count
                
        max_count = 0
        for i in range(1, 27):
            max_count = max(max_count, helper(i))
        
        return max_count
