class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        rem_nums = []
        for i in range(1, n):
            fact *= i
            rem_nums.append(str(i))
        rem_nums.append(str(n))
        res = ""
        k -= 1
        while True:
            res += rem_nums.pop(int(k // fact))
            if not rem_nums:
                break
            k %= fact
            fact //= len(rem_nums)
        return res