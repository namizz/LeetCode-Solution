class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        direction = [(-1,-1),(-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,1),(1,-1)]
        row = len(img)
        col = len(img[0])
        matrix = [[0]*len(img[0]) for _ in range(len(img))]
        for r in range(row):
            for c in range(col):
                total = img[r][c]
                count = 1
                for dr,dc in direction:
                    rr = dr+r
                    cc = dc+c
                    if 0 <= rr < row and 0 <= cc < col:
                        count += 1
                        total += img[rr][cc]  
                matrix[r][c] = total//count
        return matrix

                    


        