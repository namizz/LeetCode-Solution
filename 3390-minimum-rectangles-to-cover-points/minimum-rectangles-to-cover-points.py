class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        arr = []
        for i in range(len(points)):
            arr.append(points[i][0])
        arr.sort()
        last_p = -1
        r = 0
        for i in arr:
            if i > last_p:
                last_p = i + w
                r += 1
        return r


        