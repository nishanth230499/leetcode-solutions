class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        mem = [{} for _ in range(len(candidates))]
        def rec(i, l_target, not_considered):
            if l_target == 0:
                return [[]]
            if i == len(candidates):
                return []
            # if l_target in mem[i]:
            #     return mem[i][l_target]
            new_not_considered = set(not_considered)
            new_not_considered.add(candidates[i])
            res1 = rec(i+1, l_target, new_not_considered)
            if candidates[i] <= l_target and candidates[i] not in not_considered:
                mem[i][l_target] = res1+map(lambda a: [candidates[i]]+a, rec(i+1, l_target-candidates[i], not_considered))
            else:
                mem[i][l_target] = res1
            return mem[i][l_target]
        return rec(0, target, set())
        