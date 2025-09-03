class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        return bisect_left(range(1, max(quantities)+1), -n, key=lambda a: -sum(ceil(q/a) for q in quantities)) + 1
