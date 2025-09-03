class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem = [None] * len(nums)
        def rec(i):
            if i == len(nums)-1:
                return 0
            if mem[i] != None:
                return mem[i]
            min_hop = float("inf")
            for j in range(nums[i]):
                if i+j+1 == len(nums):
                    break
                hop = rec(i+j+1)
                if hop < min_hop:
                    min_hop = hop
            mem[i] = min_hop + 1
            # print(i, mem[i])
            return mem[i]
        
        return rec(0)
        # return 0

            
        