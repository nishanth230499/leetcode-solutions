class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parseNum(s):
            if_img = False
            real = ""
            img = ""
            for c in s:
                if c == "+":
                    if_img = True
                elif c == "i":
                    pass
                elif if_img:
                    img += c
                else:
                    real += c
            return (int(real), int(img))
        
        num1 = parseNum(num1)
        num2 = parseNum(num2)

        real = num1[0] * num2[0] - num1[1] * num2[1]
        img = num1[0] * num2[1] + num1[1] * num2[0]
        return str(real) + "+" + str(img) + "i"
