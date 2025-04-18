class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def bound(r,c):
            return 0<= r < len(mat) and 0 <= c < len(mat[0])
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')
        direction = [(-1,0),(0,1),(1,0),(0,-1)]
        # for i in range(len(mat)):
        #     print(*mat[i])
        print(queue)
        while queue:
            r,c = queue.popleft()
            for dr,dc in direction:
                    rr = dr + r
                    cc = dc + c
                    if bound(rr,cc) and mat[rr][cc] > mat[r][c]+1:
                        mat[rr][cc] = mat[r][c] + 1
                        queue.append((rr,cc))

        # print("")
        # for i in range(len(mat)):
        #     print(*mat[i])
        return mat
                    
                
                    


        