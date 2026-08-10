class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int("".join([i for i in str(n)][::-1]))
        ans = 0
        def is_prime(x):
            for i in range(2, x):
                if not x%i:
                    return False
                if i * i > x:
                    break
                
            return True
        for i in range(2, 1001):
            if is_prime(i) and min(r,n) <= i <= max(n,r):
                ans += i
            elif i > max(r,n):
                break
        return ans


        