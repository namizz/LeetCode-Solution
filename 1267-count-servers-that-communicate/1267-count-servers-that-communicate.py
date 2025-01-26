class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # grid = [[]] :List->m*n
        # two servers communicate with each other if they are on the same row or col
        # return number of servers that communicate
        # number of communicating server cannot be greater than the total number of the server
        # count the row if they have more than 1 server
        # count the col if they have more than 1 server
        row = [0] * len(grid)
        col = [0] * len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    row[r] += 1
                    col[c] += 1
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and(row[r] > 1 or col[c] > 1):
                    ans += 1
        return ans
        