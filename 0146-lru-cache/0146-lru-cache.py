class Node: 
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1 
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key,value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            lru_key = self.head.next.key
            self.remove(self.head.next)
            del self.cache[lru_key]
    
    def remove(self, n:Node):
        n.prev.next = n.next
        n.next.prev = n.prev
    
    def insert(self, n:Node):
        prev_node = self.tail.prev
        prev_node.next = n
        n.prev = prev_node
        n.next = self.tail
        self.tail.prev = n

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)