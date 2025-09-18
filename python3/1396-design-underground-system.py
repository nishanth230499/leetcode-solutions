class UndergroundSystem:

    def __init__(self):
        self.total_time = defaultdict(lambda: [0, 0])
        self.pending_journies = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.pending_journies[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.pending_journies[id]
        self.total_time[(startStation, stationName)][0] += t - startTime
        self.total_time[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t, c = self.total_time[(startStation, endStation)]
        return t / c


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)