class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if (m*n == r*c):
            reshape = []
            i1, i2 = 0,0
            j1 = 0
            while i2 < r:
                j2 = 0
                arr = []
                while j2 < c:
                    if i1 < m and j1 < n:
                        arr.append(mat[i1][j1])
                        j2 += 1
                        j1 += 1
                    else:
                        i1 += 1
                        j1 = 0
                reshape.append(arr)
                i2 += 1
            return reshape
        return mat


        