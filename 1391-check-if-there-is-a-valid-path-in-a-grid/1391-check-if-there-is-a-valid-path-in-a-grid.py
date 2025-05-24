class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        
        direction = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }

        def check(x, y):
            return 0 <= x < row and 0 <= y < col

        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            x, y = queue.popleft()
            if x == row - 1 and y == col - 1:
                return True

            for dx, dy in direction[grid[x][y]]:
                xx, yy = x + dx, y + dy
                if check(xx, yy) and (xx, yy) not in visited:
                    if opposite[(dx, dy)] in direction[grid[xx][yy]]:
                        visited.add((xx, yy))
                        queue.append((xx, yy))

        return False
