class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        temp = n - 1
        front = True
        while temp < time:
            time -= temp
            front = not(front)
        if front:
            return time + 1
        return n - time