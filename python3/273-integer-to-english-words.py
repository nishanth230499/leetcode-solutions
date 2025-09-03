class Solution:
    def threeDigitNumberToWords(self, num: int) -> str:
        num_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }
        if num % 100:
            if num % 100 in num_map:
                res = num_map[num % 100]
            else:
                res = f"{num_map[(num % 100) - (num % 10)]} {num_map[num%10]}"
        else: 
            res = ""
        if num // 100:
            res = f" {res}" if res else ""
            res = f"{num_map[num // 100]} Hundred{res}"
        return res


    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        stages = {
            0: "",
            1: " Thousand ",
            2: " Million ",
            3: " Billion ",
            4: " Trillion "
        }
        
        res = ""
        stage = 0
        while num:
            if num % 1000:
                res = f"{self.threeDigitNumberToWords(num % 1000)}{stages[stage]}{res}"
            stage += 1
            num = num // 1000
        return res.strip()
        

