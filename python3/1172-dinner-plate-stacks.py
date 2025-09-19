class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.empty_stacks = []
        self.stacks = []

    def push(self, val: int) -> None:
        while self.empty_stacks and self.empty_stacks[0] >= len(self.stacks):
            heapq.heappop(self.empty_stacks)
        if not self.empty_stacks:
            self.stacks.append([])
            heapq.heappush(self.empty_stacks, len(self.stacks) - 1)
        stack_index = self.empty_stacks[0]
        self.stacks[stack_index].append(val)
        if len(self.stacks[stack_index]) == self.capacity:
            heapq.heappop(self.empty_stacks)

    def pop(self) -> int:
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks:
            return -1
        stack = self.stacks[index]
        if not stack:
            return -1
        if len(stack) == self.capacity:
            heapq.heappush(self.empty_stacks, index)
        res = stack.pop()
        while index >= 0 and index == len(self.stacks) - 1 and not self.stacks[index]:
            index -= 1
            self.stacks.pop()
        return res



# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)