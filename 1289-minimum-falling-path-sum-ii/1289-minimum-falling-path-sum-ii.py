class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # dp[i][j] = min sum to reach cell (i, j)
        dp = [row[:] for row in grid]  # copy first row

        for i in range(1, n):
            for j in range(n):
                min_prev = min(dp[i-1][k] for k in range(n) if k != j)
                dp[i][j] += min_prev
        return min(dp[-1])