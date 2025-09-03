class TimeMap:

    def __init__(self):
        self.store = {}
    
    def bin_search(self, key, timestamp):
        if self.store[key][0][0] > timestamp:
            return -1
        if self.store[key][-1][0] <= timestamp:
            return len(self.store[key])-1
        l = 0
        r = len(self.store[key])-1
        while l+1<r:
            m = (l+r)//2
            if self.store[key][m][0] == timestamp:
                return m
            elif self.store[key][m][0] < timestamp:
                l = m
            else:
                r = m
        return l

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            m = self.bin_search(key, timestamp)
            if m == -1:
                self.store[key].insert(0, [timestamp, value])
            else:
                self.store[key].insert(m+1, [timestamp, value])
        else:
            self.store[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            m = self.bin_search(key, timestamp)
            if m == -1:
                return ""
            else:
                return self.store[key][m][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)