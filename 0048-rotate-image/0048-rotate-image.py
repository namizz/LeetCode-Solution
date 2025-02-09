class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(rows):
            lp, rp = 0, cols-1
            while lp < rp:
                matrix[i][lp], matrix[i][rp] = matrix[i][rp], matrix[i][lp]
                lp += 1
                rp -= 1
        