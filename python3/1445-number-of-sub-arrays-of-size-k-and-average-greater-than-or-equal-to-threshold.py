class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = 0
        e = k-1
        count = 0
        sum = 0
        for i in range(k):
            sum += arr[i]
        while True:
            if sum / k >= threshold:
                count += 1
            sum -= arr[s]
            s += 1
            e += 1
            if e >= len(arr):
                break
            sum += arr[e]
        return count
