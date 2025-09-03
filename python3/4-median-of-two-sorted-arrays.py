class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)

        # if len2 > len1:
        #     return self.findMedianSortedArrays(nums2, nums1)
        
        k = (len1 + len2) // 2

        low = max(0, k - len(nums2))
        high = min(k, len(nums1))

        while low <= high:
            mid = (low + high) // 2
            cut1 = mid
            cut2 = k - mid

            if cut1 == 0:
                l1 = float("-inf")
            else:
                l1 = nums1[cut1-1]
            if cut1 == len1:
                r1 = float("inf")
            else:
                r1 = nums1[cut1]
            if cut2 == 0:
                l2 = float("-inf")
            else:
                l2 = nums2[cut2-1]
            if cut2 == len2:
                r2 = float("inf") 
            else:
                r2 = nums2[cut2]

            if l1 <= r2 and l2 <= r1:
                if (len1 + len2) % 2 == 0:
                    m1 = max(l1,l2)
                    m2 = min(r1,r2)
                    return float(m1+m2)/2
                else:
                    return min(r1, r2)
            if l2 > r1:
                low = mid + 1
            else:
                high = mid - 1
        return 0
            