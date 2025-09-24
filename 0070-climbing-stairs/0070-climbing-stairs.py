class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def rec(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in cache:
                return cache[i]
            a = rec(i+1)
            b = rec(i+2)
            cache[i] = (a+b)
            return cache[i]
        return rec(0)
            

        