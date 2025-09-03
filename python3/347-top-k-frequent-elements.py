class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        counts = []
        for num in count:
            counts.append({'n': num, 'c': count[num]})
        counts.sort(key=lambda a: a['c'], reverse = True)
        counts = counts[:k]
        counts = map(lambda a: a['n'], counts)
        return counts
        