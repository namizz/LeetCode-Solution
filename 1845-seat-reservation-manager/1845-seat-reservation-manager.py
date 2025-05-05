class SeatManager:

    def __init__(self, n: int):
        self.h = []
        self.contain = set()
        for i in range(n):
            heapq.heappush(self.h, i+1)    
            self.contain.add(i+1)    

    def reserve(self) -> int:
        x = heapq.heappop(self.h)
        self.contain.remove(x)
        return x
        

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber not in self.contain:
            heapq.heappush(self.h, seatNumber)
            self.contain.add(seatNumber)

        
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)