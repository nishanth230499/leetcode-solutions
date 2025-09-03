class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ""
        repeat = max(2*numRows - 2, 1)
        iterations = len(s) // repeat + 1
        for i in range(numRows):
            if i == 0:
                for j in range(iterations):
                    if j * repeat < len(s):
                        res+=s[j*repeat]
            elif i == numRows - 1:
                for j in range(iterations):
                    if j * repeat + numRows - 1 < len(s):
                        res+=s[j * repeat + numRows - 1]
            else:
                for j in range(iterations):
                    if j * repeat + i < len(s):
                        res+=s[j * repeat + i]
                    if (j+1) * repeat - i < len(s):
                        res+=s[(j+1) * repeat - i]
        
        return res