class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c_dict = Counter(nums)
        count = 0
        for a in c_dict:
            b = a+k
            if b in c_dict:
                if a == b:
                    count += (c_dict[b] * (c_dict[b] - 1) / 2)
                else:
                    count += (c_dict[a] * c_dict[b])
        return count
