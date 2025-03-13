class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        temp = deque()
        while len(self.queue) != 1:
            temp.append(self.queue.popleft())
        x = self.queue.popleft()
        self.queue = temp
        return x        
    def top(self) -> int:
        return self.queue[-1]
        
    def empty(self) -> bool:
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()