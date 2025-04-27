class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque([(sr,sc)])
        direction = [(-1,0),(0,-1),(1,0),(0,1)]
        def inbound(r,c):
            return 0 <= r < len(image) and 0 <= c < len(image[0])
        visited = set()
        org = image[sr][sc]
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if image[r][c] != org:
                    continue
                image[r][c] = color
                visited.add((r,c))
                for dr, dc in direction:
                    rr = dr+r
                    cc = dc+c
                    if inbound(rr,cc) and (rr,cc) not in visited:
                        queue.append((rr,cc))
        return image



        