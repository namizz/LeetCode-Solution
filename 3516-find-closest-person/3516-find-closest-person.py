class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1= abs(x-z)
        dist2= abs(y-z)
        if dist1 == dist2:
            return 0
        return 1 if dist1 < dist2 else 2
        