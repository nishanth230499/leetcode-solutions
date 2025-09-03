class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack):
                    popped_char = stack.pop()
                    if not((popped_char == "(" and char == ")") or (popped_char == "[" and char == "]") or (popped_char == "{" and char == "}")):
                        return False

                else:
                    return False
        return not(bool(len(stack)))
        