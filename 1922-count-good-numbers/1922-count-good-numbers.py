class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def fast(x,p):
            ans = 1
            while p > 0:
                if p%2:
                    ans = (ans*x)%(10**9+7)
                x = (x*x)%(10**9+7)
                p //=2
            return ans
            

        even = (n+1)//2
        odd = n//2
        return fast(5,even) * fast(4,odd) % (10**9+7)

        