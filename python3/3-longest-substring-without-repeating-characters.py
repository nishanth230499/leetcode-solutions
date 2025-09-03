class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        max_len = 0
        start = 0
        end = 1
        last_seen = {}
        last_seen[s[0]] = 0
        while start < len(s) - max_len:
            while end < len(s):
                if last_seen.get(s[end], -1) >= start:
                    max_len = max(max_len, end-start)
                    start = last_seen[s[end]] + 1
                    last_seen[s[end]] = end
                    end = end + 1
                    break
                else:
                    last_seen[s[end]] = end
                    end = end + 1
            max_len = max(max_len, end-start)
        return max_len