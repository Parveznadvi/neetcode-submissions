class Node:
    def __init__(self, key:int, value: int):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.cache={}
        self.lru=Node(-1,-1)
        self.mru=Node(-1,-1)
        self.lru.next=self.mru
        self.mru.prev=self.lru    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        returnNode = self.cache[key]
        returnNode.next.prev=returnNode.prev
        returnNode.prev.next=returnNode.next
        returnNode.next=self.mru
        returnNode.prev=self.mru.prev
        self.mru.prev.next=returnNode
        self.mru.prev=returnNode
        return returnNode.value        

    def put(self, key: int, value: int) -> None:
        # Key already exists -> Update value & move to MRU
        if key in self.cache:
            existingNode=self.cache[key]
            existingNode.value=value

            existingNode.prev.next=existingNode.next
            existingNode.next.prev=existingNode.prev

            existingNode.next=self.mru
            existingNode.prev=self.mru.prev
            self.mru.prev.next = existingNode
            self.mru.prev = existingNode
            return

        # Key is brand-new -> Check capacity before adding 
        if self.size==self.capacity:
            deleteNode=self.lru.next
            del self.cache[deleteNode.key]
            # Updating LRU
            self.lru.next=self.lru.next.next
            self.lru.next.prev=self.lru
            self.size-=1

        # Insert the brand-new node at the MRU end
        newNode = Node(key, value)
        self.cache[key]=newNode
        self.size+=1
        newNode.next=self.mru
        newNode.prev=self.mru.prev
        self.mru.prev.next = newNode
        self.mru.prev = newNode




        # if self.size<self.capacity:
        #     newNode = Node(key, value)
        #     self.size+=1
        #     self.cache[key]=newNode            
        #     newNode.next=self.mru
        #     newNode.prev=self.mru.prev
        #     self.mru.prev.next = newNode
        #     self.mru.prev = newNode
        # else:            
        #     if key not in self.cache:
        #         deleteNode=self.lru.next
        #         del self.cache[deleteNode.key]
        #     # Updating LRU
        #     self.lru.next=self.lru.next.next
        #     self.lru.next.prev=self.lru
        #     # Inserting 3,30 in the end
        #     newNode = Node(key, value)
        #     self.cache[key]=newNode
        #     newNode.next=self.mru
        #     newNode.prev=self.mru.prev
        #     self.mru.prev.next = newNode
        #     self.mru.prev = newNode
            



            

        
