class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # mat=[[]], target =[[]]
        # rotate(mat) => target
        # [[0,1,2],
        #  [3,4,5],
        #  [6,7,8]]
        n = len(mat)

        def rotate_90(mat):
            for i in range(n):
                for j in range(i):
                    mat[j][i], mat[i][j] = mat[i][j], mat[j][i]
            for i in range(n):
                l = 0
                r = n - 1
                while l < r:
                    mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
                    l += 1
                    r -= 1
            return mat

        for _ in range(4):
            if rotate_90(mat) == target:
                return True
        return False
