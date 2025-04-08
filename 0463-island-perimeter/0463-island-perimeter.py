class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # visited = [[False]*col for _ in range(row)]
        # print(visited)

        direction = [(-1,0),(0,-1),(1,0),(0,1)]
        ans = 0
        def bound(rr,cc):
            return 0 <= rr < row and 0<= cc < col
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    ans += 4
                    for dr,dc in direction:
                        rr = dr + r
                        cc = dc + c
                        if bound(rr,cc) and grid[rr][cc]:
                            ans -= 1
        return ans



        