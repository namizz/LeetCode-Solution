class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        arr = []
        for i in range(len(points)):
            arr.append(points[i][0])
        arr.sort()
        last_p = -1
        i = 0
        r = 0
        while i < len(arr):
            if arr[i] <= last_p:
                i += 1
            else:
                last_p = arr[i] + w
                r += 1
        return r


        