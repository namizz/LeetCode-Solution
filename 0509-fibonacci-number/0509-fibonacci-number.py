class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = self.fib(n-1) + self.fib(n-2)
            return cache[n]
        return dp(n)
        