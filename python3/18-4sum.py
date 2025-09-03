class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        op = []
        nums.sort()
        for i in range(0, len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                
                l = j+1
                r = len(nums)-1

                while l<r:
                    new_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if new_sum == target:
                        op.append([nums[i], nums[j], nums[l], nums[r]])
                    
                    if new_sum > target:
                        old_r = nums[r]
                        while l<r and nums[r] == old_r:
                            r -= 1
                        continue
                    
                    old_l = nums[l]
                    while l<r and nums[l] == old_l:
                        l += 1
        return op
        