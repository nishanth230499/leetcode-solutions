class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        return bisect_left(range(1, max(nums)), -maxOperations, key=lambda a: -sum(ceil(num/a)-1 for num in nums)) + 1