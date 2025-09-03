class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        q = deque()
        res = []
        for r in range(len(nums)):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)

            if r >= k:
                if q[0] == l:
                    q.popleft()
                l += 1
            if r >= k-1:
                res.append(nums[q[0]])
        return res