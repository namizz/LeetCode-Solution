class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]
        self.size = 0       

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
            self.size = 0
        else:
            self.arr.append(num * self.arr[-1])
            self.size += 1
        print(self.arr)

        

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return self.arr[-1]//self.arr[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)