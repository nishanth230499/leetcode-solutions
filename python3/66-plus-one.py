class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += add
            add = digits[i] // 10
            digits[i] %= 10
            if add == 0:
                break
        if add == 1:
            return [1] + digits
        return digits