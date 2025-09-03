class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        str_len = len(words)*len(words[0])
        sub_str_len = len(words[0])

        res = []
        
        i = 0
        while i < len(s) - str_len + 2:
            j = i
            words_dict = {}
            for word in words:
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
            while words_dict:
                next_word = s[j:j+sub_str_len]
                # print(i, j, next_word, words_dict)
                if next_word in words_dict:
                    if words_dict[next_word] > 1:
                        words_dict[next_word] -= 1
                    else:
                        del words_dict[next_word]
                    j += sub_str_len
                else:
                    break
            if j == i + str_len:
                res.append(i)
                i += 1
            else:
                i += 1
        return res


        