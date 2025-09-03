class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_end_map = {}
        end_start_map = {}
        v = set()
        for num in nums:
            if num in v:
                continue
            v.add(num)
            if num - 1 in end_start_map:
                start_end_map[end_start_map[num - 1]] = num
                end_start_map[num] = end_start_map[num - 1]
                del end_start_map[num - 1]
            else:
                start_end_map[num] = num
                end_start_map[num] = num
            if num + 1 in start_end_map:
                start_end_map[end_start_map[num]] = start_end_map[num + 1]
                end_start_map[start_end_map[num + 1]] = end_start_map[num]
                del end_start_map[num]
                del start_end_map[num + 1]
        max_len = 0
        for start, end in start_end_map.items():
            max_len = max(max_len, end - start + 1)
        return max_len
