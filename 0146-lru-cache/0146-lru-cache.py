class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def insert(self,node):
        node.next = self.left.next
        node.prev = self.left
        self.left.next.prev = node
        self.left.next = node        
    
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1
              

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key] = Node(key,value)
        self.insert(self.hashmap[key])
        if len(self.hashmap) > self.capacity:
            LRU = self.right.prev
            self.remove(LRU) 
            del self.hashmap[LRU.key] 
        
         


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)