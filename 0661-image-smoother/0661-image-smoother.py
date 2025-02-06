class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        direction = [
            (-1, -1),
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1),
            (1, 1),
            (-1, 1),
            (1, -1),
        ]
        row = len(img)
        col = len(img[0])
        # after computing make the average*256+number and if the number > 256 make a %256 an find the number
        for r in range(row):
            for c in range(col):
                total = img[r][c]%256
                count = 1
                for dr, dc in direction:
                    rr = dr + r
                    cc = dc + c
                    if 0 <= rr < row and 0 <= cc < col:
                        total += (img[rr][cc] % 256)
                        count += 1
                total = total//count
                img[r][c] = (total*256 + img[r][c])
        for r in range(row):
            for c in range(col):
                img[r][c] //= 256
        return img

