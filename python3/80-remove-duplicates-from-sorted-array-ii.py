class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        duplicate_count = 0
        duplicate_num = None
        for num in nums:
            if duplicate_num == num:
                if duplicate_count < 2:
                    nums[i] = num
                    i += 1
                    duplicate_count += 1
                else:
                    continue
            else:
                duplicate_num = num
                duplicate_count = 1
                nums[i] = num
                i += 1
        return i