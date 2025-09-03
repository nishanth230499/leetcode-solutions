class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_i = None
        max_j = None
        max_vol = 0
        while i < j:
            if max_i is not None and height[i] < height[max_i]:
                i = i+1
                continue
            if max_i is None:
                max_i = i
            if max_j is not None and height[j] < height[max_j]:
                j = j - 1
                continue
            if max_j is None:
                max_j = j
            
            width = j - i
            h = min(height[i], height[j])

            vol = width * h

            if vol > max_vol:
                max_vol = vol

            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
            
        return max_vol
        