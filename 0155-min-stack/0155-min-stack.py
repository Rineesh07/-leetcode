class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        self.topp = -1
    def push(self, value: int) -> None:
        self.topp += 1
        self.stack.append(value)
        if not self.minstack :
            self.minstack.append(value)
        else:
            self.minstack.append(min(value,self.minstack[-1]))
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()