class RandomizedSet:

    def __init__(self):
        self.contain = {}
        self.l = []
        

    def insert(self, val: int) -> bool:
        if val in self.contain:
            return False
        self.contain[val] = len(self.l)
        self.l.append(val)
        return True
    def remove(self, val: int) -> bool:  
        if val not in self.contain:
            return False
        r_l = self.contain[val]
        self.l[r_l], self.l[-1] = self.l[-1], self.l[r_l]
        del self.contain[self.l[-1]]
        self.l.pop()
        return True
    def getRandom(self) -> int:
        return self.l[randint(0, len(self.l)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()