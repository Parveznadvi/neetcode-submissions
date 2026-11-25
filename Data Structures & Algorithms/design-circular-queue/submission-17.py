class MyCircularQueue:

    def __init__(self, k: int):
        self.arr=[-1] * k
        self.front=0
        self.rear=0
        self.size=0
        self.length=k        

    def enQueue(self, value: int) -> bool:
        if self.size==self.length:
            return False  
        self.arr[self.rear]=value
        self.size+=1 
        self.rear=(self.rear+1) % self.length
        return True
        # if self.rear!=self.length:
        #     self.arr[self.rear]=value
        #     self.size+=1 
        #     if self.rear<=self.length-1:
        #         self.rear+=1
        #     if self.rear==self.length and self.front!=0:
        #         self.rear=0
        #     return True

    def deQueue(self) -> bool:
        if self.size==0:
            return False  
        self.arr[self.front]=-1
        self.size-=1 
        self.front=(self.front+1) % self.length
        return True
        # if self.front!=self.length:
        #     self.arr[self.front]=-1
        #     self.size-=1 
        #     if self.front<=self.length-1:
        #         self.front+=1
        #         if self.rear==self.length:
        #             self.rear=0       
        #     if self.front==self.length and self.rear!=0:
        #         self.front=0
        #     return True

    def Front(self) -> int:
        if self.size==0:
            return -1
        return self.arr[self.front]
        # if self.front==self.length and self.rear!=0:
        #     return self.arr[0]
        # if self.front!=self.length:
        #     return self.arr[self.front]
        

    def Rear(self) -> int:
        if self.size==0:
            return -1
        # return self.arr[self.rear-1]
        return self.arr[(self.rear - 1 + self.length) % self.length]
        

    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size==self.length:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()