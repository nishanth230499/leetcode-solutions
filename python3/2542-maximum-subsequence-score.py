class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        num2_sorted = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        num2_sorted.sort(key = lambda a: a[1], reverse = True)
        
        res = 0
        q = []
        num1_total = 0

        for i in range(len(num2_sorted)):
            heapq.heappush(q, num2_sorted[i])
            num1_total += num2_sorted[i][0]

            if len(q) > k:
                num1_total -= heapq.heappop(q)[0]
            
            if len(q) == k:
                res = max(res, num2_sorted[i][1] * num1_total)
        
        return res