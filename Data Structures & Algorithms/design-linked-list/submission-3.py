class ListNode:
    def __init__(self, val: int):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index: int) -> int:
        if self.size==0 or index>=self.size:
            return -1
        result=self.head
        count=0
        while(result.next!=None and count<index):
            result=result.next
            count+=1
        return result.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.size==0:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode 
        self.size+=1
        
    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.size==0:
            self.head=newNode
        else:
            result=self.head
            while(result.next!=None):
                result=result.next
            result.next=newNode
        self.size+=1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        elif index==self.size:
            self.addAtTail(val)
            return
        elif index>self.size:
            return
        newNode = ListNode(val)
        result=self.head
        count=1
        while(result.next!=None and count<index):
            result=result.next
            count+=1
        newNode.next=result.next
        result.next=newNode
        self.size+=1        

    def deleteAtIndex(self, index: int) -> None:
        if self.size==0:
            return
        if index==0:
            self.head=self.head.next
            return
        result=self.head
        count=1
        while(result.next!=None and count<index):
            result=result.next
            count+=1
        if result.next==None:
            return
        # if result.next.next!=None:
        result.next=result.next.next
        self.size-=1
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)