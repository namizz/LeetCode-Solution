class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        rang = 0
        while left < right:
            left >>= 1
            right >>= 1
            rang += 1
        ans = right << rang
        return ans

        
        