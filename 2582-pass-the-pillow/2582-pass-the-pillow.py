class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        return time%(n-1)+1 if (time//(n-1))%2 == 0 else n - (time%(n-1))
        