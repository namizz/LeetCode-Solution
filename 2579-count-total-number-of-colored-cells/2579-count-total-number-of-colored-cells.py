class Solution:
    def coloredCells(self, n: int) -> int:
        return 5 + ((((n-2)*(n-1))//2) + (n-2))*4 if n != 1 else 1

        