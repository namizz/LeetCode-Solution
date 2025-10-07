class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        _max = 0
        n = len(grid)
        # find the max and min of the grid
        for arr in grid:
            cmax = max(arr)
            _max = max(cmax, _max)
        direction = [(1,0), (0,1), (-1,0),(0,-1)]
        def answer(value):
            visited = set()
            def findpath(r,c):
                if (r,c) == (len(grid)-1, len(grid[0])-1):
                    return True
                
                visited.add((r,c))
                for dr, dc in direction:
                    rr = dr + r
                    cc = dc + c
                    if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and (rr,cc) not in visited:
                        if grid[rr][cc] <= value:
                            if findpath(rr,cc):
                                return True
                return False
            return grid[0][0] <= value and findpath(0,0)
        
        l = grid[0][0]
        r = _max
        ans = float(inf)
        while l <= r:
            mid = (l+r)//2
            if answer(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
            print(ans, l, r)
        return ans 
        