class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.outerBucket = [Node(-1,-1) for _ in range(1000)]
        
    def find(self, key: int) -> Node:
        firstHash = key % 1000
        prev = self.outerBucket[firstHash]
        while prev.next != None:
            cur = prev.next
            if cur.key == key:
                return prev
            else:
                prev = cur
        return prev
    
    def put(self, key: int, value: int) -> None:
        prev = self.find(key)
        if prev.next == None:
            prev.next = Node(key,value)
        else:
            prev.next.value = value
        
    def get(self, key: int) -> int:
        prev = self.find(key)
        if prev.next != None:
            return prev.next.value
        else:
            return -1

    def remove(self, key: int) -> None:
        prev = self.find(key)
        if prev.next != None:
            cur = prev.next
            prev.next = cur.next
            cur.next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)