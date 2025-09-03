class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for string in strs:
            string_set = ''.join(sorted(string))
            if string_set not in groups:
                groups[string_set] = [string]
            else:
                groups[string_set].append(string)
        
        return groups.values()

        