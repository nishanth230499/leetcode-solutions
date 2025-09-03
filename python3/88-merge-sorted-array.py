class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = m + n - 1
        mr = m - 1
        nr = n - 1

        while nr >= 0:
            if mr < 0 or nums2[nr] > nums1[mr]:
                nums1[r] = nums2[nr]
                nr -= 1
            else:
                nums1[r] = nums1[mr]
                mr -= 1
            r -= 1
            
        