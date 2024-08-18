class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [[0]*3 for i in range(3)]
        counter = 0
        for i in range(len(moves)):
            a,b = moves[i]
            counter += 1
            if i%2 == 0:
                matrix[a][b] = 1 
            else:
                matrix[a][b] = 2
        print(matrix)
        for i in range(3):
            if matrix[i][0] and matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2]:
                print('l')
                return "A" if matrix[i][0]== 1 else "B"
            elif matrix[0][i] and matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i]:
                print('k')
                return "A" if matrix[0][i]== 1 else "B"
        if matrix[1][1] and ((matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] )or (matrix[2][0] == matrix[1][1] and matrix[1][1] == matrix[0][2])):
            return "A" if matrix[1][1]== 1 else "B" 
        else:
            return 'Draw' if counter == 9 else 'Pending'
            