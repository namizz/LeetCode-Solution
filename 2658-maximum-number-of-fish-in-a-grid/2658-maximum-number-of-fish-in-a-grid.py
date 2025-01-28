class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # grid = [[]]
        # return maximum number of fish a fisher can catch
        # if grid[r][c] = 0--> land
        # if grid[r][c] > 0---> water with grid[r][c] fish/es 
        # we are going to use depth search or/and breath search
        # set of visted node
        # start from the start and add in to queue 
        # if pop is not in queue when we pop from the node != 0 go deepandu
        # store in visited node
        # go through unvisted node
        # ````````````
        # queue, visited = [()], go through
        n_r = len(grid)
        n_c = len(grid[0])
        visited = set()
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def bfs(r,c):
            queue = deque([(r, c)])
            visited.add((r,c))
            ans = grid[r][c]

            while queue:
                tr,tc = queue.popleft()
                for dr, dc in direction:
                    rr = dr + tr
                    cc = dc + tc
                    if 0 <= rr < n_r and 0 <= cc < n_c and (rr,cc) not in visited and grid[rr][cc] > 0:
                        queue.append((rr, cc))
                        visited.add((rr,cc))
                        ans += grid[rr][cc]
            return ans
        ans = 0
        for r in range(n_r):
            for c in range(n_c):
                if (r,c) not in visited and grid[r][c] > 0:
                    
                    ans = max(ans, bfs(r,c))

        return ans
            
        

        