class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[1]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    break
                up = mat[i-1][j] if i > 0 else 0                
                left = mat[i][j-1] if j > 0 else 0
                mat[i][j] = up + left
        for i in range(m):
            print(mat[i])
        return mat[m-1][n-1]

        