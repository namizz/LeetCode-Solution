class MyQueue:

    def __init__(self):
        self.stack = []
        self.t = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if len(self.stack) > self.t:
            self.t += 1
            return self.stack[self.t-1]
        

    def peek(self) -> int:
        if len(self.stack) > self.t:
            return self.stack[self.t]
        

    def empty(self) -> bool:
        if len(self.stack) > self.t:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()