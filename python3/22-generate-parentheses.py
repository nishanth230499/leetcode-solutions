class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = [["(", 1, 0]]
        while len(stack):
            ele = stack.pop()
            if ele[1] == ele[2] == n:
                output.append(ele[0])
                continue
            if ele[1] != n:
                stack.append([ele[0]+"(", ele[1]+1, ele[2]])
            if ele[2] < ele[1]:
                stack.append([ele[0]+")", ele[1], ele[2]+1])
        return output
            

        