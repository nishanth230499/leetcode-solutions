class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = 0
        nbits = 0
        for num in nums:
            if num >= 0:
                bits ^= 2 ** num
            else:
                nbits ^= 2 ** (-num)
        return int(math.log(bits, 2)) if bits else -int(math.log(nbits, 2))