class MyHashSet:

    def __init__(self): 
        self.outerBucket = [None] * 1000

    def add(self, key: int) -> None:
        firstHash = key % 1000
        secondHash = key // 1000
        if self.outerBucket[firstHash] == None:
            if firstHash==0:
                self.outerBucket[firstHash] = [False] * 1001
            else:
                self.outerBucket[firstHash] = [False] * 1000
        self.outerBucket[firstHash][secondHash] = True
        return None

    def remove(self, key: int) -> None:
        firstHash = key % 1000
        secondHash = key // 1000
        if self.outerBucket[firstHash] == None:
            return None
        self.outerBucket[firstHash][secondHash] = False
        return None
        
    def contains(self, key: int) -> bool:
        firstHash = key % 1000
        secondHash = key // 1000
        if self.outerBucket[firstHash] == None:
            return False
        return self.outerBucket[firstHash][secondHash] == True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)