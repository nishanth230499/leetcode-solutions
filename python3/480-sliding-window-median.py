import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums

        heap_left = []
        heap_right = []

        heap_left_extra = []
        heap_right_extra = []

        for num in nums[:k]:
            heapq.heappush(heap_left, -heapq.heappushpop(heap_right, num))
            if len(heap_left) > len(heap_right):
                heapq.heappush(heap_right, -heapq.heappop(heap_left))
        
        if k % 2:
            res = [heap_right[0]]
        else:
            res = [(-heap_left[0] + heap_right[0]) / 2]

        for i, r in enumerate(nums[k:]):
            l = nums[i]

            if l >= heap_right[0]:
                if r < heap_right[0]:
                    r = -heapq.heappushpop(heap_left, -r)
                heapq.heappush(heap_right, r)
                heapq.heappush(heap_right_extra, l)
            else:
                if r >= heap_right[0]:
                    r = heapq.heappushpop(heap_right, r)
                heapq.heappush(heap_left, -r)
                heapq.heappush(heap_left_extra, -l)

            while heap_left_extra and heap_left_extra[0] == heap_left[0]:
                heapq.heappop(heap_left)
                heapq.heappop(heap_left_extra)
            while heap_right_extra and heap_right_extra[0] == heap_right[0]:
                heapq.heappop(heap_right)
                heapq.heappop(heap_right_extra)
            
            if k % 2:
                res.append(heap_right[0])
            else:
                res.append((-heap_left[0] + heap_right[0]) / 2)
        
        return res
            