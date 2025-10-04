class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        mat = [[0]*col for i in range(row)]
        for i in range(col):
            mat[0][i] = matrix[row-1][i]
        for r in range(1,row):
            for c in range(col):
                val = min(mat[r-1][c], mat[r-1][c-1] if c > 0 else float(inf), mat[r-1][c+1] if c+1 < col else float(inf))
                if val == float(inf):
                    val = 0
                mat[r][c] = matrix[row-r-1][c] + val
        # for i in range(row):
        #     print(mat[i])
        return min(mat[row-1])
        