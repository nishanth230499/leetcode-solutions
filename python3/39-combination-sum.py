class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return [[]] if target == 0 else []
        sol = self.combinationSum(candidates[1:], target)
        if candidates[0] <= target:
            sol += map(lambda a: [candidates[0]]+a, self.combinationSum(candidates, target-candidates[0]))
        return sol