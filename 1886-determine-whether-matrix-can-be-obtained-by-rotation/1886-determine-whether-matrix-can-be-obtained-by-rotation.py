class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # mat=[[]], target =[[]]
        # rotate(mat) => target
        # [[0,1,2],
        #  [3,4,5],
        #  [6,7,8]]
        n = len(mat)
        def rotate_90(mat):
            transpose = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    transpose[j][i] = mat[i][j]
            for i in range(n):
                l = 0
                r = n-1
                while l < r:
                    transpose[i][l], transpose[i][r] = transpose[i][r], transpose[i][l]
                    l += 1
                    r -= 1
            return transpose
        for i in range(n):
            if rotate_90(mat) == target:
                return True
            else:
                mat = rotate_90(mat)
        return False