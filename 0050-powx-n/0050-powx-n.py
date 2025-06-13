class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}
        def power(x,n):
            if n == 1:
                return x
            if n == 0:
                return 1 
            if n in cache:
                return cache[n]
            mid = n//2
            r = n%2
            p1 = power(x, mid) 
            p2 = power(x, mid+r)
            cache[n] = p1*p2
            return cache[n]
        return power(x,n) if n >= 0 else 1/power(x,-n)

        