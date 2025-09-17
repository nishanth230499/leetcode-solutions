class MapSum:

    def __init__(self):
        self.map_sum = defaultdict(int)
        self.store = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.store:
            for i in range(len(key)):
                self.map_sum[key[:i+1]] -= self.store[key]
        for i in range(len(key)):
            self.map_sum[key[:i+1]] += val
        self.store[key] = val

    def sum(self, prefix: str) -> int:
        return self.map_sum[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)