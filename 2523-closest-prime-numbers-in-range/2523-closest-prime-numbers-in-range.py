class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def primes(n):
            p = [True] *(n+1)
            p[0] = p[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if p[i]:
                    for j in range(i * i, n + 1, i):
                        p[j] = False
            return p
        ans = primes(right)
        prime = [i for i in range(left, right + 1) if ans[i]]
        
        a = [-1, -1]
        for i in range(len(prime) - 1):
            if a[0] == -1 or prime[i + 1] - prime[i] < a[1] - a[0]:
                a[0] = prime[i]
                a[1] = prime[i + 1]

        return a

        