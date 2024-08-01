class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dir = {0: 'East', 1: 'North', 2: 'West', 3: 'South'}
        self.row = 0
        self.column = 0
        self.direction = 0

    def step(self, num: int) -> None:
        i = 0
        cell = (self.width + self.height-2)*2
        if num >= cell:
            num %= cell
            if self.row == 0 and self.column == 0:
                self.direction = 3

        while i < num:
            if self.column < self.width - 1 and self.row == 0:
                self.direction = 0
                self.column += 1
                i += 1
            elif self.column == self.width - 1 and self.row < self.height - 1:
                self.direction = 1
                self.row += 1
                i += 1
            elif self.column > 0 and self.row == self.height - 1:
                self.direction = 2
                self.column -= 1
                i += 1
            elif self.column == 0 and self.row > 0:
                self.direction = 3
                self.row -= 1
                i += 1
            else:
                self.direction = 0

    def getPos(self) -> List[int]:
        return [self.column, self.row]

    def getDir(self) -> str:
        return self.dir[self.direction]
        
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()