class MyQueue:

    def __init__(self):
        self.MainStack = []
        self.SubStack = []

    def push(self, x: int) -> None:
        self.MainStack.append(x)

    def pop(self) -> int:
        self.SubStack.clear()
        for i in self.MainStack:
            self.SubStack.append(i)
        self.SubStack.reverse()
        poped = self.SubStack.pop()
        self.MainStack.clear()
        for i in self.SubStack:
            self.MainStack.append(i)
        self.MainStack.reverse()
        return poped

    def peek(self) -> int:
        self.SubStack.clear()
        for i in self.MainStack:
            self.SubStack.append(i)
        self.SubStack.reverse()
        peeked = self.SubStack[-1]
        return peeked

    def empty(self) -> bool:
        if len(self.MainStack) == 0:
            return True
        else: return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()