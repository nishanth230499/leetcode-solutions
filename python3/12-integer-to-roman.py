class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""

        res += "M"*(num//1000)
        num = num % 1000

        res += "D"*(num//500)
        num = num % 500

        res += "C"*(num//100)
        num = num % 100

        res += "L"*(num//50)
        num = num % 50

        res += "X"*(num//10)
        num = num % 10

        res += "V"*(num//5)
        num = num % 5

        res += "I"*num

        # print(res)
        res = res.replace("IIII", "IV")
        res = res.replace("VIV", "IX")
        res = res.replace("XXXX", "XL")
        res = res.replace("LXL", "XC")
        res = res.replace("CCCC", "CD")
        res = res.replace("DCD", "CM")

        return res
            # MDCCCCLXXXXIIII
        