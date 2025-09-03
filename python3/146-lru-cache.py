class Node:
    def __init__(self, key = None, prev = None, next = None):
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.ll_map = {}
        self.ll_head = Node()
        self.ll_tail = Node()
        self.ll_head.next = self.ll_tail
        self.ll_tail.prev = self.ll_head

    def inc_priority(self, key):
        current = self.ll_map[key]
        current.prev.next = current.next
        current.next.prev = current.prev
        self.ll_tail.prev.next = current
        current.prev = self.ll_tail.prev
        current.next = self.ll_tail
        self.ll_tail.prev = current

    def add_key(self, key, value):
        self.store[key] = value
        current = Node(key)
        self.ll_map[key] = current
        self.ll_tail.prev.next = current
        current.prev = self.ll_tail.prev
        current.next = self.ll_tail
        self.ll_tail.prev = current
    
    def remove_lru(self):
        current = self.ll_head.next
        del self.store[current.key]
        del self.ll_map[current.key]
        self.ll_head.next = current.next
        current.next.prev = current.prev
        del current
        
    def get(self, key: int) -> int:
        if key in self.store:
            self.inc_priority(key)
            return self.store[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = value
            self.inc_priority(key)
        else:
            if self.capacity:
                self.add_key(key, value)
                self.capacity -= 1
            else:
                self.remove_lru()
                self.add_key(key, value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)