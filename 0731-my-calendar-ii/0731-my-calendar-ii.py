class MyCalendarTwo:

    def __init__(self):
        self.one = []
        self.two = []

        

    def book(self, startTime: int, endTime: int) -> bool:
        for st,end in self.two:
            if max(st,startTime) < min(endTime,end):
                return False
        for st,end in self.one:
            if max(st,startTime) < min(endTime,end):
                start = max(st, startTime)
                endT = min(end, endTime)
                self.two.append([start, endT])
        self.one.append([startTime, endTime])

        return True


        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)