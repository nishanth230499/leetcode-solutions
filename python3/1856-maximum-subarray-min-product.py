class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)
        
        stack = []
        res = 0

        for i, num in enumerate(nums + [float("-inf")]):
            while stack and stack[-1][1] >= num:
                _, l_num = stack.pop()
                l = stack[-1][0] if stack else -1 
                res = max(res, l_num*(prefix[i] - prefix[l+1]))
            stack.append((i, num))
        
        return res % 1000000007

