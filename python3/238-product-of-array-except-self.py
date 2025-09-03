class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
        if zeros == 0:
            prod = 1
            for num in nums:
                if num != 0:
                    prod *= num
            return list(map(lambda a: prod/a, nums))
        elif zeros == 1:
            prod = 1
            for num in nums:
                if num != 0:
                    prod *= num
            return list(map(lambda a: prod if a==0 else 0, nums))
        else:
            return list(map(lambda a: 0, nums))
        

        