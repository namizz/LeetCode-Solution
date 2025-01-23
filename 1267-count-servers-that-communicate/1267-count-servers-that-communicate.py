class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = [0] * len(grid[0])
        cols = [0] * len(grid)

        # Count servers in each row and each column
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    rows[c] += 1
                    cols[r] += 1

        ans = 0

        # Count servers that can communicate (in the same row or column)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    if rows[c] > 1 or cols[r] > 1:
                        ans += 1

        return ans
        