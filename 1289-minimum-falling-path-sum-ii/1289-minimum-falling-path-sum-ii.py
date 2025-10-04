class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        mat = [i[:] for i in grid]
        for r in range(1,row):
            for c in range(col):
                val = min(mat[r-1][i] for i in range(col) if i != c)
                mat[r][c] += val
        # for i in range(row):
        #     print(mat[i])
        return min(mat[-1])