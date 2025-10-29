class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 0
        while n:
            n >>= 1
            ans <<= 1
            ans |= 1
        
        return ans
        