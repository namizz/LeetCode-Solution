class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = [[0]*(len(grid[0])-2) for _ in range(len(grid)-2)]
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                _max = 0
                for r in range(3):
                    for c in range(3):
                        _max = max(grid[r+i][c+j], _max)
                ans[i][j] = _max
        return ans


        
        

        