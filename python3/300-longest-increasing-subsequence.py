class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # mem = [1 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             mem[i] = max(mem[i], mem[j] + 1)
        # return max(mem)

        lis_index = [-1 for _ in range(len(nums))]

        lis_index[0] = 0
        max_lis = 1
        for i, num in enumerate(nums):
            if i == 0:
                continue
            # print(lis_index, max_lis, list(map(lambda a: 0 if nums[a] < num else 1, lis_index)))
            index = bisect.bisect_right(lis_index, 0, lo = 0, hi = max_lis, key=lambda a: 0 if nums[a] < num else 1)
            # print(index)
            lis_index[index] = i
            max_lis = max(max_lis, index + 1)
        
        return max_lis