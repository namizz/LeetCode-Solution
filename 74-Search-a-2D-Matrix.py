class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        lp , rp = 0, (row*col) - 1
        print(row, col, lp, rp)
        while lp <= rp:
            mid = (lp+rp)//2
            r = mid//col
            c = mid%col
            print(lp, rp, matrix[r][c])
            if matrix[r][c] > target:
                rp = mid - 1
            elif matrix[r][c] < target:
                lp = mid + 1
            else:
                return True
        return False
        