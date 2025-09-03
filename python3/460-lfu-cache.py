class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.freq = 0
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.keyToNode = {}
        self.minFreq = 0
        self.freqToList = defaultdict(DLL)

    def touch(self, key):
        node = self.keyToNode[key]
        dll = self.freqToList[node.freq]
        node.prev.next = node.next
        node.next.prev = node.prev
        if dll.head.next == dll.tail:
            del dll
            if node.freq == self.minFreq:
                self.minFreq += 1
        node.freq += 1
        dll = self.freqToList[node.freq]
        node.next = dll.head.next
        dll.head.next = node
        node.prev = dll.head
        node.next.prev = node


    def get(self, key: int) -> int:
        if key in self.keyToNode:
            self.touch(key)
            return self.keyToNode[key].value
        return -1

    def print(self):
        pass
        # print("-")
        # for key in self.keyToNode:
        #     print(key, self.keyToNode[key].value, self.keyToNode[key].freq)
        # print("freqmap")
        # for freq in self.freqToList:
        #     dll = self.freqToList[freq]
        #     print(freq)
        #     cur = dll.head.next
        #     while cur != dll.tail:
        #         print(cur.key, cur.freq)
        #         cur = cur.next

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key not in self.keyToNode and len(self.keyToNode) == self.cap:
            dll = self.freqToList[self.minFreq]
            node = dll.tail.prev
            node.prev.next = node.next
            node.next.prev = node.prev
            if dll.head.next == dll.tail:
                del dll
                while self.minFreq not in self.freqToList:
                    self.minFreq += 1
            del self.keyToNode[node.key]
        self.print()
        if key not in self.keyToNode:
            node = Node(key, value)
            self.keyToNode[key] = node
            self.minFreq = 0
            dll = self.freqToList[0]
            dll.head.next = node
            dll.tail.prev = node
            node.prev = dll.head
            node.next = dll.tail
        self.keyToNode[key].value = value
        self.touch(key)
        self.print()
            



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)