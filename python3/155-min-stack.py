class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        ele = {'val': val}
        ele['min'] = min(val, self.stack[-1]['min'] if len(self.stack) else val)
        self.stack.append(ele)

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()['val']

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]['val']

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1]['min']


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()