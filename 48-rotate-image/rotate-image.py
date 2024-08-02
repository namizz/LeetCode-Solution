class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        column = len(matrix[0])
        for i in range(column):
            for j in range(row):
                if j <=i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[0]) - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right],matrix[i][left]
                left += 1
                right -= 1

        return matrix