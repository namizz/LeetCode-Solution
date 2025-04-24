class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # if region O is surrounded by X change them to X
        # find O and make a dfs call 
        # check if it's not edge cell(return condition 1)
        # no connected O(return condition 2)
        direction = [(-1,0),(0,-1),(1,0),(0,1)]

        def inbound(r,c):
            return 0 <= r < row and 0<= c <col
        def dfs(r,c):
            if not inbound(r,c) or board[r][c] != 'O':
                return
            if board[r][c] == 'O':
                visited.add((r,c))
            for dr,dc in direction:
                rr = r + dr
                cc = c + dc
                if (rr,cc) not in visited:
                    dfs(rr,cc)
        visited = set()
        row = len(board)
        col = len(board[0])
        for r in range(row):
            if board[r][0] == 'O':
                dfs(r,0)
                visited.add((r,0))
            if board[r][col-1] == 'O':
                dfs(r,col-1)
                visited.add((r,col-1))

        for c in range(col):
            if board[0][c] == 'O':
                dfs(0,c)
                visited.add((0,c))
            if board[row-1][c] == 'O':
                dfs(row-1,c)
                visited.add((row-1,c))
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X' 
        