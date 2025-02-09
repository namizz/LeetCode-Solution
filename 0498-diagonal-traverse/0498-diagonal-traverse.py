class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        def downward(_sum, i):
            while _sum > 0:#mat[i][_sum]
                if 0<= i < rows and 0 <= _sum < cols:
                    ans.append(mat[i][_sum])
                _sum -= 1
                i += 1
            if 0<= i < rows and 0 <= _sum < cols:
                ans.append(mat[i][_sum]) 
        def upward(_sum, i):
            while _sum > 0:
                if 0<= _sum < rows and 0 <= i < cols:
                    ans.append(mat[_sum][i])
                _sum -= 1
                i += 1
            if 0<= _sum < rows and 0 <= i < cols:
                    ans.append(mat[_sum][i])
        rows, cols = len(mat), len(mat[0])
        _sum, i = 0, 0
        down = False
        while _sum < rows+cols-1:
            if down:
                downward(_sum, i)
            else:
                upward(_sum, i)
            _sum += 1
            down = not down
        return ans
                

        