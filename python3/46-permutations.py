class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def rec(arr):
            if len(arr) == 1:
                return [[arr[0]]]
            soln = []
            rem = arr[-1]
            for per in rec(arr[:-1]):
                soln.extend([per[:i]+[rem]+per[i:] for i in range(len(per)+1)])
            return soln

        return rec(nums)