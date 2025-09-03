class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s = 0
        rs = []
        for num in nums:
            s += num
            rs.append(s)
        ans = 0
        sorted_rs = []
        for num in rs:
            if lower <= num <= upper:
                ans += 1
            l = bisect_left(sorted_rs, num-upper)
            r = bisect_right(sorted_rs, num-lower)
            ans += (r-l)
            insort(sorted_rs, num)
        return ans