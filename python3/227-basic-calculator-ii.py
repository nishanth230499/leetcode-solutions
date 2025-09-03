class Solution:
    def calculate(self, s: str) -> int:
        def norm(n):
            if n > 0:
                return int(math.floor(n))
            if n%1:
                return int(math.ceil(n))
            return n
        
        stack = []

        for c in s:
            if c != " ":
                if c == "+" or c == "-" or c == "*" or c == "/":
                    stack.append(c)
                elif stack and type(stack[-1]) == int:
                    stack.append(stack.pop() * 10 + int(c))
                else:
                    stack.append(int(c))
        
        stack1 = []
        for c in stack:
            if stack1 and stack1[-1] == "*":
                stack1.pop()
                c1 = stack1.pop()
                stack1.append(norm(c1 * c))
            elif stack1 and stack1[-1] == "/":
                stack1.pop()
                c1 = stack1.pop()
                stack1.append(norm(c1 / c))
            else:
                stack1.append(c)

        res = stack1[0]
        for i in range(1, len(stack1), 2):
            sign = stack1[i]
            num = stack1[i+1]
            if sign == "+":
                res += num
            else:
                res -= num
        return int(res)
        
        