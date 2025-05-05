class SeatManager:

    def __init__(self, n: int):
        self.h = []
        for i in range(n):
            heapq.heappush(self.h, i+1)    

    def reserve(self) -> int:
        x = heapq.heappop(self.h)
        return x
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.h, seatNumber)

        
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)