class MyStack:

    def __init__(self):
        self.Mainqueue = []
        self.Subqueue = []

    def push(self, x: int) -> None:
        self.Mainqueue.append(x)
        return self.Mainqueue
            
    def pop(self) -> int:
        for i in self.Mainqueue:
            self.Subqueue.append(i)
        self.Subqueue.reverse()
        poped = self.Subqueue.pop(0)
        self.Mainqueue.clear()
        for i in self.Subqueue:
            self.Mainqueue.append(i)
        self.Subqueue.clear()
        self.Mainqueue.reverse()
        return poped

    def top(self) -> int:
        for i in self.Mainqueue:
            self.Subqueue.append(i)
        self.Subqueue.reverse()
        top = self.Subqueue[0]
        self.Subqueue.clear()
        return top

    def empty(self) -> bool:
        print(self.Mainqueue)
        if len(self.Mainqueue) == 0:
            return True
        else: return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()