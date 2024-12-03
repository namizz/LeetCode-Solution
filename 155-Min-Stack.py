class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []
        

    def push(self, val: int) -> None:
        minimum = 0
        self.arr.append(val)
        if len(self.min) == 0:
            self.min.append(val)
            minimum = val
        else:
            minimum = min(val, self.min[len(self.min)-1])
            self.min.append(minimum)
        

    def pop(self) -> None:
        self.arr.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.arr[len(self.arr)-1]
        

    def getMin(self) -> int:
        return self.min[len(self.min)-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()