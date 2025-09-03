class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        cur = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums) - 2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while l<r:
                new_sum = nums[i] + nums[l] + nums[r]
                # print(i, l, r, new_sum)
                if new_sum == target:
                    return target
                
                if abs(new_sum - target) < abs(cur - target):
                    cur = new_sum
                
                if new_sum < target:
                    l += 1
                    continue
                
                if new_sum > target:
                    r -= 1

        return cur
        