class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        nums = self.countAndSay(n-1)
        last_c = None
        count = 0
        res = ""
        for c in nums:
            if c == last_c:
                count+=1
            else:
                if last_c == None:
                    last_c = c
                    count = 1
                else:
                    res += str(count) + last_c
                    last_c = c
                    count = 1
        res += str(count) + last_c
        return res





        
        