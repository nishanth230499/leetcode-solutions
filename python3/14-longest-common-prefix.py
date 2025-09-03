class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        max_len = min(map(len, strs))
        soln = ""
        for i in range(max_len):
            if all(map(lambda a: a[i] == strs[0][i], strs)):
                soln = soln + strs[0][i]
            else:
                break
        return soln
        