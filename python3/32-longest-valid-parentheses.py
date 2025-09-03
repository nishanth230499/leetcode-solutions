class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        scores_at_index = {}
        cur_score = 0
        for i in range(len(s)):
            if s[i] == "(":
                cur_score += 1
            elif s[i] == ")":
                cur_score -= 1
            if cur_score not in scores_at_index:
                scores_at_index[cur_score] = (i,)
            else:
                scores_at_index[cur_score] += (i,)
        
        cur_score = 0
        max_len = 0
        for i in range(len(s)):
            end_index = None
            if cur_score - 1 in scores_at_index and len(scores_at_index[cur_score-1]):
                end_index = scores_at_index[cur_score-1][0]
            elif cur_score in scores_at_index and len(scores_at_index[cur_score]):
                end_index = scores_at_index[cur_score][-1] + 1
            if end_index != None:
                str_len = end_index - i
                if str_len > max_len:
                    max_len = str_len
            if s[i] == "(":
                cur_score += 1
            elif s[i] == ")":
                cur_score -= 1
            scores_at_index[cur_score] = scores_at_index[cur_score][1:]
        
        return max_len
            


        