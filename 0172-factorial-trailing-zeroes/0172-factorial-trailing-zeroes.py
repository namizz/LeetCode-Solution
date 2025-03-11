class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n < 5:
                return 0
            return n//5 + fact(n//5)
        return fact(n)
        
        