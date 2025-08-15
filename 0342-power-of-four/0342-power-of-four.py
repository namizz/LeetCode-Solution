class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 3:
            n /=4
        return n == 1
        