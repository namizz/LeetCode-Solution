class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        for i in range(32):
            if (n >> i) & 1:
                m |= 1 << (32-i-1) 
        return m
        

        