class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ["0"]*(len(num1) + len(num2))

        def add_num(n, i):
            num = int(res[-1-i])
            num += n
            res[-1-i] = str(num%10)
            num //= 10
            if num:
                add_num(num, i+1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                a = int(num1[-1-i])
                b = int(num2[-1-j])
                add_num(a*b, i+j)
        
        for i in range(len(res)-1):
            if res[i] == "0":
                res[i] = ""
            else:
                break
        return "".join(res)