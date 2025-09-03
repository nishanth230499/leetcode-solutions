class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        l_max = height[i]
        r_max = height[j]
        qty = 0
        while i<j:
            if l_max < r_max:
                i += 1
                l_max = max(l_max, height[i])
                qty += max(l_max - height[i], 0)
            else:
                j -= 1
                r_max = max(r_max, height[j])
                qty += max(r_max - height[j], 0)
        return qty


        