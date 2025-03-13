class MyQueue:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        temp = []
        print(self.stack)
        while self.stack:
            temp.append(self.stack.pop())
        x = temp.pop()
        print(temp)
        self.stack = []
        while temp:
            self.stack.append(temp.pop())
        return x

    def peek(self) -> int:
        return self.stack[0]

        

    def empty(self) -> bool:
        return not self.stack
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()