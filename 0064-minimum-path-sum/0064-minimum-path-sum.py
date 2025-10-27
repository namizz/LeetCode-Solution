class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def boundary(x,n):
            return 0 <= x < n
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        
        for r in range(len(grid)-1,-1,-1):
            for c in range(len(grid[0])-1,-1,-1):
                x,y = float(inf), float(inf)
                if boundary(r+1, len(grid)):
                    y = dp[r+1][c]
                if boundary(c+1, len(grid[0])):
                    x = dp[r][c+1] 
                if x == float(inf) and y == float(inf):
                    dp[r][c] = grid[r][c] 
                else:
                    dp[r][c] = grid[r][c] + min(x,y)
            # for i in dp:
            #     print(i)
            # print("")
        return dp[0][0]



        
        