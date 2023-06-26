class MinStack:

    def __init__(self):
        self.minVal = []
        self.Stack = []

    def push(self, val: int) -> None:
        self.Stack.append(val)
        if self.minVal:
            val = min(val, self.minVal[-1])
        self.minVal.append(val)

    def pop(self) -> None:
        self.Stack.pop()
        self.minVal.pop()
        
    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return int(self.minVal[-1])
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()