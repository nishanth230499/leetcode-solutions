class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_count = {}
        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1

        num_keys = list(nums_count.keys())
        num_keys.sort()

        res = []
        for num1 in num_keys:
            for num2 in num_keys:
                if num2 > num1 or (num2 == num1 and nums_count[num1] > 1):
                    num3 = -(num1 + num2)
                    if (num3 > num2 or (num3 == num2 and [num1, num2, num3].count(num2) <= nums_count[num2])) and num3 in nums_count:
                        res.append([num1, num2, num3])
        
        # if 0 in nums_count and nums_count[0] > 2:
        #     res.append([0,0,0])
        return res
        

        