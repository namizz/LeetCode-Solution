class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x1,x2,y1,y2):
            return abs(x1-x2)+abs(y1-y2)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[ry] = rx
            return True
        
        e = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = distance(points[i][0], points[j][0], points[i][1], points[j][1])
                e.append((dist, i, j))
        e.sort()

        parent = [i for i in range(len(points))]

        ans = 0
        for d,st,ed in e:
            if union(st,ed):
                ans += d
        return ans
        