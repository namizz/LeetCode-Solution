class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])
        queue = deque()
        height = [[0]*row for _ in range(col)]
        visited = set()
        for r in range(row):
            for c in range(col):
                if isWater[r][c]:
                    visited.add((r,c))
                    queue.append((r,c))
        direction = [(-1,0),(0,-1),(1,0),(0,1)]
        while queue:
            r,c = queue.popleft()
            for dr, dc in direction:
                rr = r+dr
                cc = c+dc
                if (rr,cc) not in visited and( 0 <= rr < row and 0 <= cc < col):
                    height[rr][cc] = height[r][c] + 1
                    visited.add((rr,cc))
                    queue.append((rr,cc))
        return height 


        

        