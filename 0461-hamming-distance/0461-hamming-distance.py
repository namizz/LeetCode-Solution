class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xy = x^y
        ans = 0
        while xy:
            if xy&1:
                ans += 1
            xy >>= 1
        return ans
        