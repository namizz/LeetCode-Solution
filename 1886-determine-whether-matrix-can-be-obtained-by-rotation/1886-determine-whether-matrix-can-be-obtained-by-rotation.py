class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # mat=[[]], target =[[]]
        # rotate(mat) => target
        # [[0,1,2],
        #  [3,4,5],
        #  [6,7,8]]
        n = len(mat)

        def rotate_90(mat):
            rotated = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated[j][n-1-i] = mat[i][j]
            print(rotated)
            return rotated

        for _ in range(4):
            if rotate_90(mat) == target:
                return True
            else:
                mat = rotate_90(mat)
        return False
