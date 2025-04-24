class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # mxn
        # M-> bomb
        # E-> empty
        # B-> no adjectent mine
        # X-> explode bomb
        # [r,c]-> clicked is M -> change to 'X'
        # else: ->reveal all
        def inbound(r,c):
            return 0 <= r < len(board) and 0 <= c < len(board[0]) 
        def dfs(r,c):
            if not inbound(r,c) or board[r][c] != "E":
                return 
            count = 0
            for dr,dc in direction:
                rr = r+dr
                cc = c+dc
                if inbound(rr,cc) and board[rr][cc] == "M":
                    count += 1
            if count > 0:
                board[r][c] = str(count)
            else:
                board[r][c] = "B"
                for dr,dc in direction:
                    rr = r+dr
                    cc = c+dc
                    dfs(rr,cc)
            

        x,y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        direction = [(-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1)]
        dfs(x,y)
        return board
        