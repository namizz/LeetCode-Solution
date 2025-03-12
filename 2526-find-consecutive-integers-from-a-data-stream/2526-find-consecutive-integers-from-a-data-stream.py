class DataStream:

    def __init__(self, value: int, k: int):
        self.arr = deque()
        self.v = value
        self.k = k
        

    def consec(self, num: int) -> bool:
        while self.arr and self.arr[0] != num:
            self.arr.popleft()
        self.arr.append(num)
        if len(self.arr) >= self.k and (self.arr and self.arr[0] == self.v):
            return True
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)