class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = sorted(map(lambda a: str(a), nums), reverse=True, key=lambda a: a*10)
        if arr[0] == "0":
            return "0"
        return "".join(arr)