class Solution:
    def countPrimes(self, n: int) -> int:
        def prime(x):
            d = 2
            while d*d <= x:
                if not x%d:
                    return False
                d += 1
            return True
        ans = 0
        for i in range(2,n):
            if prime(i):
                ans += 1
        return ans

        