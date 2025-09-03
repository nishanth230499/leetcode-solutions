class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def rec2(s, e, c):
            if s + c > e + 1:
                return []
            if c == 1:
                return [[i] for i in range(s, e+1)]
            soln = []
            for i in range(s, e+1):
                par = [[i]+per for per in rec2(i+1, e, c-1)]
                soln.extend(par)
            return soln

        def rec(arr):
            if len(arr) == 1:
                return [[arr[0]]*count[arr[0]]]
            soln = []
            rem = arr[-1]
            # print(arr)
            for per in rec(arr[:-1]):
                # print(0, len(per) + count[rem] - 1, count[rem])
                for indices in rec2(0, len(per) + count[rem] - 1, count[rem]):
                    # print(indices)
                    s = []
                    a = 0
                    b = 0
                    for i in range(len(per) + count[rem]):
                        # print(i)
                        if a < len(indices) and i == indices[a]:
                            s.append(rem)
                            a += 1
                        else:
                            s.append(per[b])
                            b += 1
                    soln.append(s)
            return soln

        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        return rec(list(count.keys()))
        