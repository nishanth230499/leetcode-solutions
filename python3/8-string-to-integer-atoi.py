class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ""
        space_read = False
        sign_read = False
        for c in s:
            if c == " ":
                if space_read:
                    break
                else:
                    continue
            else:
                space_read = True

                if c == "+" or c == "-":
                    if sign_read:
                        break
                    else:
                        res += c
                        sign_read = True
                        continue
                else:
                    sign_read = True
                    if c <= "9" and c >= "0":
                        res += c
                    else:
                        break
                
        res = int(0 if res in ["" , "+", "-"] else res)
        if res < 0:
            return max(res, -2 ** 31)
        else:
            return min(res, 2 ** 31 -1)
        