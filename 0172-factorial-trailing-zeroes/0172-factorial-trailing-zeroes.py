class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        def fact(n):
            if n <= 1:
                return 1
            return n*fact(n-1)
        temp = fact(n)
        while temp%10 == 0:
            ans += 1
            temp//= 10

        return ans
        