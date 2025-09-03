class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        max_str = ""
        len_s = len(s)
        i = 0
        while i < len_s:
            j = 0
            while j < len_s // 2 + 1:
                left = i - j - 1
                right = i + j + 1
                if left < 0 or right >= len_s or s[left] != s[right]:
                    if 2*j+1 > max_len:
                        max_len = 2*j+1
                        max_str = s[left+1 : right]
                    break
                else:
                    j = j + 1
            
            j = 0
            while j < len_s // 2 + 1:
                left = i - j
                right = i + 1 + j
                if left < 0 or right >= len_s or s[left] != s[right]:
                    if 2*j > max_len:
                        max_len = 2*j
                        max_str = s[left+1 : right]
                    break
                else:
                    j = j + 1
            i = i + 1
        return max_str
                    



        