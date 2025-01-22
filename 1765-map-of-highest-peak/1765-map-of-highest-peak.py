class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # land and water
        # isWater = [[]]
        # 0->land 1->water
        # return height[[]]
        # height >= 0
        # water height = 0
        # two adjacent must have an absolute height difference of <= 1
        # [1,2,0]
        # [0,1,2]
        # [1,2,3]
        queue = deque()
        row = len(isWater)
        col = len(isWater[0])
        height = [[-1 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    queue.append((r,c))
        print(queue)
        direction = [(0,-1),(0,1),(1,0),(-1,0)]
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in direction:
                r = dr+cr
                c = cc+dc
                if 0 <= r < row and 0<= c < col and height[r][c] == -1:
                    height[r][c] = height[cr][cc] + 1
                    queue.append((r,c))
        return height


        