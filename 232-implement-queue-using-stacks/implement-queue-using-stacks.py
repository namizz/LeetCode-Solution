class MyQueue:

    def __init__(self):
        self.queue = []
        self.pointer = 0
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        if self.queue:
            self.pointer += 1
            return self.queue[self.pointer-1]


        

    def peek(self) -> int:
        return self.queue[self.pointer]
        

    def empty(self) -> bool:
        return (len(self.queue) == self.pointer)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()