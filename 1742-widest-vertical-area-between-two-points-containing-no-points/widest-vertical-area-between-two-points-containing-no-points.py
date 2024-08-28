class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = []
        for a,b in points:
            x_points.append(a)
        x_points.sort()
        ans = 0
        for i in range(len(x_points)-1):
            ans = max(ans, x_points[i+1]-x_points[i])
        return ans

        