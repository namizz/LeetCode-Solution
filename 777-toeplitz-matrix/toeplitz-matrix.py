class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        cols = len(matrix[0])
        row = len(matrix)
        #check diagonals across row
        k = 0
        while k + 1 < row:
            i = k
            j = 0
            while j + 1 < cols and i + 1 < row:
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                i += 1
                j += 1
            k += 1
        #check diagonals across cols
        k = 0
        while k + 1 < cols:
            j = k
            i = 0
            while j + 1 < cols and i + 1 < row:
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                i += 1
                j += 1
            k += 1
        
        return True

        