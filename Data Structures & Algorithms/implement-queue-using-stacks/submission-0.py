class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if self.outStack:
            return self.outStack.pop()
        else:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
            return self.outStack.pop()

    def peek(self) -> int:
        if self.outStack:
            return self.outStack[-1]
        elif self.inStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
            return self.outStack[-1]

    def empty(self) -> bool:
        if self.outStack or self.inStack:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()