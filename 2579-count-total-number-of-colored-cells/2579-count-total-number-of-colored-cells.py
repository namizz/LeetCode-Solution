class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        ans = 1
        for i in range(3,n+1):
            ans += (i-2)*4
            ans += 4
        return ans + 4




        
        return pow(horz-2,2)+4
        