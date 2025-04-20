class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        rot = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    rot += 1
        # print(rot)
        # print(queue)
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            temp = []
            if rot:
                ans += 1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in direction:
                    rr = dr + r
                    cc = dc + c
                    if 0<= rr < row and 0 <= cc < col and grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        rot -= 1
                        queue.append((rr,cc))
            if not rot:
                return ans
        return -1 if rot else 0 
                


        