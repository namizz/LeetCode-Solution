class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # flow:
        # if the top, bottom , right, left is less than or equal to the current cell the water can flow
        # two edge(top right, bottom left) are flow to bothe pacific and atlantic ocean
        # top and left edge cells flow to pacific
        # bottom and right edge cells flow to atlantic 
        # any cell neighbour to the edge cell if their height is greater than the cell at the edge if flow one of the oceans
        # dfs on the neighbour cell that can flow the rain water to edges cells
        row = len(heights)
        col = len(heights[0])
        mat = [[0]*col for _ in range(row)]
        pacific = set()
        atlantic = set()
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c, ocean):
            if (r,c) in ocean:
                return
            mat[r][c] += 1
            ocean.add((r,c))
            # print(r,c, ocean)
            for dr,dc in direction:
                rr = dr + r
                cc = dc + c
                if 0 <= rr < row and 0 <= cc < col and heights[r][c] <= heights[rr][cc]:
                    dfs(rr,cc,ocean) 
        


        for i in range(col):
            dfs(0,i,pacific)
        
        for i in range(row):
            dfs(i,0,pacific)
        

        for i in range(col):
            dfs(col-1,i,atlantic)
        for i in range(row):
            dfs(i,row-1,atlantic)
        
       

        return [[r,c] for r in range(row) 
                for c in range(col) if mat[r][c] == 2]

        