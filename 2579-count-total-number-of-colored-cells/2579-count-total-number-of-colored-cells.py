class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        ans = 1
        ans += (((n-2)*(n-1))//2)*4
        ans += 4*(n-2)
        return ans + 4




        
        return pow(horz-2,2)+4
        