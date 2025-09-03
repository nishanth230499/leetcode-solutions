class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem_last_robbed = [None for _ in range(len(nums))]
        mem_last_not_robbed = [None for _ in range(len(nums))]

        def rec(i, rob):
            if i == 0:
                return 0 if rob else nums[0]
            if i == 1:
                return nums[1] if rob else max(nums[0], nums[1])
            
            if rob:
                if mem_last_robbed[i] != None:
                    return mem_last_robbed[i]
                
                mem_last_robbed[i] = max(rec(i-1, rob), rec(i-2, rob) + nums[i])
                return mem_last_robbed[i]
            else:
                if mem_last_not_robbed[i] != None:
                    return mem_last_not_robbed[i]
                mem_last_not_robbed[i] = max(rec(i-1, rob), rec(i-2, rob) + nums[i])
                return mem_last_not_robbed[i]
        
        # max(rec(len(nums)-2, False), rec(len(nums)-3, True) + nums[-1])

        # print(mem_last_robbed)
        # print(mem_last_not_robbed)

        num_len = len(nums)
        return max(rec(num_len-2, False) if num_len-2>=0 else 0, (rec(num_len-3, True) if num_len-3>=0 else 0) + nums[-1])

            
