class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        row, col = len(grid), len(grid[0])
        mrow, mcol = 3*row, 3*col
        mgrid = [[0]*mcol for _ in range(mrow)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "/":
                    mgrid[r*3][c*3+2] = 1
                    mgrid[r*3 +1][c*3+1] = 1
                    mgrid[r*3 +2][c*3] = 1
                elif grid[r][c] == "\\":
                    mgrid[r*3][c*3] = 1
                    mgrid[r*3+1][c*3+1] = 1
                    mgrid[r*3+2][c*3+2] = 1
        def check(r,c):
            return 0 <= r < mrow and 0 <= c <mcol 
        def dfs(r,c):
            if (r,c) in visited:
                return 
            visited.add((r,c))
            for dr,dc in directions:
                rr = dr + r
                cc = dc + c
                if check(rr,cc) and mgrid[rr][cc] == 0:
                    dfs(rr,cc)


        visited = set()
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        ans = 0
        for r in range(mrow):
            for c in range(mcol):
                if (r,c) not in visited and mgrid[r][c] == 0:
                    dfs(r,c)
                    ans += 1
        return ans

        