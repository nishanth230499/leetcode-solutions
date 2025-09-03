class Solution:
    def countBits(self, n: int) -> List[int]:
        mem = [0 for _ in range(n+1)]
        for i in range(n+1):
            mem[i] = mem[i >> 1] + (i%2)
        return mem