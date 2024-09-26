class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
        else:
            self.min = min(self.min,val)
        self.stack.append([val, self.min])
        

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min = self.stack[-1][1]
        else:
            self.min = None


        

    def top(self) -> int:
        print(self.stack[-1])
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()