class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[len(x) - 1 - i]:
                return False
        return True
        
        