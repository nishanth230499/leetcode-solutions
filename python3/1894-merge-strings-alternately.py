class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        len1 = len(word1)
        len2 = len(word2)

        while i < len1 or i < len2:
            if i < len1:
                result.append(word1[i])
            if i < len2:
                result.append(word2[i])
            i += 1
        return ''.join(result)

        