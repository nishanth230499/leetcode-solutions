class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [None for _ in range(amount + 1)]
        mem[0] = 0
        for i in range(amount + 1):
            if mem[i] != None:
                for coin in coins:
                    if i+coin <= amount and (mem[i+coin] == None or mem[i] + 1 < mem[i+coin]):
                        mem[i+coin] = mem[i] + 1
        return mem[-1] if mem[-1] != None else -1