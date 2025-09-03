class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(lambda: 0))

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1 = point[0]
        y1 = point[1]
        for y2 in self.points[x1]:
            diff = y2 - y1
            if diff != 0:
                x2s = [x1 - diff, x1 + diff]
                for x2 in x2s:
                    if x2 in self.points and y1 in self.points[x2] and y2 in self.points[x2]:
                        res += (self.points[x1][y2] * self.points[x2][y1] * self.points[x2][y2])
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)