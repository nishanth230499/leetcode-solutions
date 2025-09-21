class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        total = 0
        res = [0, 0, float("inf")]
        for right in range(len(arr)):
            total += abs(arr[right] - x)

            if right - left + 1 > k:
                total -= abs(arr[left] - x)
                left += 1
            
            if right - left + 1 == k:
                if total < res[2]:
                    res = [left, right, total]
        
        return arr[res[0]: res[1] + 1]
