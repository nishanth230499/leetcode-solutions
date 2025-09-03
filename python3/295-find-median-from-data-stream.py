class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        temp = heapq.heappop(self.low)
        heapq.heappush(self.high, -temp)

        if len(self.high) - len(self.low) == 2:
            temp = heapq.heappop(self.high)
            heapq.heappush(self.low, -temp)

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2
        else:
            return self.high[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()